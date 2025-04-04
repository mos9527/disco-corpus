# Auto-generated by https://github.com/mos9527/UnityPyTypetreeCodegen
# Python definition for Pages.Gameplay.Journal

from .... import *
from ....Sunshine.Journal import JournalSubtaskUI
from ....Sunshine.Journal import JournalTaskUI
from ....DiscoPages.Elements.Journal import PageSystemJournalTasksScroll
from .... import TabSwitchAnimationController

@UTTCGen
class BadgePage(MonoBehaviour):
	profileMissing : PPtr[GameObject]
	profileDiscovered : PPtr[GameObject]
@UTTCGen
class JournalControllerPageSystem(MonoBehaviour):
	inBlockTitleTextColor : ColorRGBA
	outOfBlockTitleTextColor : ColorRGBA
@UTTCGen
class JournalNavigationParameters(MonoBehaviour):
	pass
@UTTCGen
class JournalPage(MonoBehaviour):
	tasksScroll : PPtr[PageSystemJournalTasksScroll]
	badgeNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	mapNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	taskPrefab : PPtr[JournalTaskUI]
	weekDayTextPrefab : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	tasksContainer : PPtr[RectTransform]
	activeDoneTabButtons : List[object] # XXX: Fallback of Button[]
	tabSwitchIndicator : PPtr[TabSwitchAnimationController]
@UTTCGen
class TaskDetailsNavigationParameters(MonoBehaviour):
	pass
@UTTCGen
class TaskDetailsPage(MonoBehaviour):
	taskTitle : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	selectedTaskFiledDateTime : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	taskStateDescription : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	taskDescriptionTextField : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	subtasksContainer : PPtr[RectTransform]
	subtaskPrefab : PPtr[JournalSubtaskUI]
