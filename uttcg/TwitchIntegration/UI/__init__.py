# Auto-generated by https://github.com/mos9527/UnityPyTypetreeCodegen
# Python definition for TwitchIntegration.UI

from ... import *

@UTTCGen
class DisableIfTwitchModeIsNotActive(MonoBehaviour):
	target : PPtr[GameObject]
@UTTCGen
class TwitchActiveStatus(MonoBehaviour):
	image : PPtr[Image]
	activeTwitch : ColorRGBA
	inactiveColor : ColorRGBA
@UTTCGen
class TwitchEnableIntegration(MonoBehaviour):
	canvasGroups : List[CanvasGroup]
	twitchIntegrationToggleOptions : PPtr[GameObject]
	moreTwitchIntegrationOptions : PPtr[GameObject]
	connectionResult : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	intergationEnabledToggle : PPtr[object] # XXX: Fallback of PPtr<Toggle>
	secretKeyField : PPtr[object] # XXX: Fallback of PPtr<TMP_InputField>
	connectToggle : PPtr[object] # XXX: Fallback of PPtr<Toggle>
@UTTCGen
class TwitchStartDialoguePoll(MonoBehaviour):
	startPoll : PPtr[object] # XXX: Fallback of PPtr<Button>
	pollInProgress : PPtr[Image]
	timer : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	canvasGroup : PPtr[CanvasGroup]
