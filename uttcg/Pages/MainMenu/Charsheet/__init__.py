# Auto-generated by https://github.com/mos9527/UnityPyTypetreeCodegen
# Python definition for Pages.MainMenu.Charsheet

from .... import *
from ....DiscoPages.Elements.Charsheet import PageSystemStatPanel
from .... import SegmentIndicator
from ....PagesSystem import SkillPortraitAnimatorHelperPageSystem
from .... import SkillPortraitOverviewPanel
from ....DiscoPages.Elements import SkillPortraitPanelPageSystem
from .... import StatPanel
from ....DiscoPages.Elements.Common import SwipeDetector
from .... import SwipeUIElementSelectionController
from .... import TabSwitchAnimationController

@UTTCGen
class CharsheetMainMenuPage(MonoBehaviour):
	stats : List[PPtr[PageSystemStatPanel]]
	portraits : List[PPtr[SkillPortraitPanelPageSystem]]
	maximizeButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	minimizeButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	swipeDetectors : List[SwipeDetector]
@UTTCGen
class CustomStatsPage(MonoBehaviour):
	abilityMethod : int
	resetButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	randomizeButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	skillsNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	ChangeColorDuration : float
	statPanels : List[StatPanel]
@UTTCGen
class SkillOverviewMainMenuPage(MonoBehaviour):
	skillInfoNavigateButtons : List[object] # XXX: Fallback of Button[]
	portraitSkillPipIndicator : PPtr[SegmentIndicator]
	skillPortraitAnimatorHelper : PPtr[SkillPortraitAnimatorHelperPageSystem]
	leftArrowButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	rightArrowButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	confirmButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	portraitOverviewPanel : PPtr[SkillPortraitOverviewPanel]
	leftPortraitOverviewPanel : PPtr[SkillPortraitOverviewPanel]
	rightPortraitOverviewPanel : PPtr[SkillPortraitOverviewPanel]
	tabSwitchAnimationController : PPtr[TabSwitchAnimationController]
	swipeAnimatorController : PPtr[SwipeUIElementSelectionController]
	infoText : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	signatureSkillButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	setSignatureButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	signatureSkillIcon : PPtr[Image]
