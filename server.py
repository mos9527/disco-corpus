import argparse, logging, os, urllib, json
from functools import lru_cache, cache
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from http import HTTPStatus
import urllib.parse

logger = logging.getLogger("server")
logger.setLevel(logging.DEBUG)


class AudioCache:
    game_dir: str = None
    vo_mapping: dict = {}
    aa_mapping: dict = {}

    def load(self, game_dir: str, vo_mapping: dict, aa_mapping: dict = None):
        self.game_dir = game_dir
        self.vo_mapping = vo_mapping
        self.aa_mapping = aa_mapping

    @lru_cache
    def read(self, convo_id, diag_id):
        import UnityPy
        from UnityPy.enums import ClassIDType

        mapped = self.vo_mapping.get(f"{convo_id + 1}.{diag_id}", None)
        if mapped is None:
            return b""
        ab = self.aa_mapping[mapped["name"]]
        bundle = os.path.join(self.game_dir, ab)
        env = UnityPy.load(bundle)
        obj = filter(lambda x: x.type == ClassIDType.AudioClip, env.objects)
        obj = [obj.read() for obj in obj]
        obj = next(obj for obj in obj if obj.m_Name == mapped["name"])
        smp = list(obj.samples.values())[0]
        return smp


audio_cache = AudioCache()


class DiscoHandler(SimpleHTTPRequestHandler):
    @property
    @cache
    def svg_template(self):
        template = os.path.join(os.path.dirname(__file__), "html", "svg_template.html")
        with open(template, "r") as f:
            return f.read()

    def svg(self, path):
        path = self.translate_path(path)
        title, cid = self.path.split("/")[-1].split("_", 2)
        title = urllib.parse.unquote(title)
        cid = cid.split(".")[0]
        content = open(path, "r", encoding="utf-8").read()
        content = content[content.index("<svg") :]
        result = self.svg_template.replace("{{title}}", title)
        result = result.replace("{{cid}}", cid)
        result = result.replace("{{svg_content}}", content)
        # html
        return HTTPStatus.OK, "text/html", result.encode("utf-8")

    def vo(self, path):
        # get convo_id and diag_id from path
        # /convo_id/diag_id.wav
        parts = path.split("/")
        convo_id, diag_id = parts[-2:]
        diag_id = diag_id.split(".")[0]
        return HTTPStatus.OK, "audio/wav", audio_cache.read(int(convo_id), int(diag_id))

    def router(self, path):
        path = path.strip("/")
        if path.lower().endswith(".svg"):
            return self.svg(path)
        if path.lower().endswith(".wav"):
            return self.vo(path)

    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            parts = urllib.parse.urlsplit(self.path)
            if not parts.path.endswith("/"):
                # redirect browser - doing basically what apache does
                self.send_response(HTTPStatus.MOVED_PERMANENTLY)
                new_parts = (parts[0], parts[1], parts[2] + "/", parts[3], parts[4])
                new_url = urllib.parse.urlunsplit(new_parts)
                self.send_header("Location", new_url)
                self.send_header("Content-Length", "0")
                self.end_headers()
                return None
            for index in self.index_pages:
                index = os.path.join(path, index)
                if os.path.isfile(index):
                    path = index
                    break
            else:
                return self.list_directory(path)

        code, mime, content = self.router(self.path)
        self.send_response(code)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Serve Disco Elysium files")
    args.add_argument("--host", help="Host to serve on", default="0.0.0.0")
    args.add_argument(
        "--port",
        help="Port to serve on",
        default=8000,
    )
    args.add_argument("--directory", help="Directory to serve from", default="svg")
    args.add_argument(
        "--aa-dir",
        help="Path to game's StreamingAssets/aa/StandaloneWindows64 directory",
        default=r"C:\Program Files (x86)\Steam\steamapps\common\Disco Elysium\disco_Data\StreamingAssets\aa\StandaloneWindows64",
    )
    args.add_argument(
        "--vo-mapping",
        help="Path to the voiceover mapping file",
        default=os.path.join(os.path.dirname(__file__), "vo_mapping.json"),
    )
    args.add_argument(
        "--aa-mapping",
        help="Path to the audio mapping file",
        default=os.path.join(os.path.dirname(__file__), "aa_mapping.json"),
    )
    args = args.parse_args()

    if args.vo_mapping and args.aa_dir and args.aa_mapping:
        with open(args.vo_mapping, "r") as f:
            vo_mapping = json.load(f)
            audio_cache.load(args.aa_dir, vo_mapping)
        with open(args.aa_mapping, "r") as f:
            aa_mapping = json.load(f)
            audio_cache.aa_mapping = aa_mapping
    else:
        logger.error("Missing AA mapping or VO mapping. Voiceovers unavailable.")
    os.chdir(args.directory)
    with ThreadingHTTPServer((args.host, args.port), DiscoHandler) as httpd:
        try:
            host, port = httpd.socket.getsockname()[:2]
            url_host = f"[{host}]" if ":" in host else host
            logger.info(
                f"Serving HTTP on {host} port {port} "
                f"> http://127.0.0.1:{port}/"
                f"> http://{url_host}:{port}/"
                f""
                f"Press Ctrl-C to stop."
            )
            httpd.serve_forever()
        except Exception as e:
            logger.info("Exiting. %s" % e)
