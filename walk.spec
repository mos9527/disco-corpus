# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata
import os
expand_cwd = lambda p: os.path.abspath(os.path.expanduser(os.path.expandvars(p)))
datas = [
    (expand_cwd("./graphviz/disco-corpus-cn"),"graphviz/disco-corpus-cn"),
    (expand_cwd("./graphviz/disco-corpus-en"),"graphviz/disco-corpus-en")
]
datas += copy_metadata('readchar')
print("extra data", datas)


a = Analysis(
    ['walk.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='disco',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=''
)
