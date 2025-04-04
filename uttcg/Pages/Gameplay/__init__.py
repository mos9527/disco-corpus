# Auto-generated by https://github.com/mos9527/UnityPyTypetreeCodegen
# Python definition for Pages.Gameplay

from ... import *
from ...DiscoPages.Elements.HUD import PageSystemHUDPortraitsAnimator
from ...DiscoPages.Elements.MainMenu import PageSystemMenuButton
from ...Sunshine.Views import StatsView
from ...DiscoPages.Elements.Common import SwipeDetector

@UTTCGen
class FakeDialogueStartPage(MonoBehaviour):
	continueButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	dialogueImage : PPtr[Image]
@UTTCGen
class GamePauseMenuPage(MonoBehaviour):
	menuItemTemplate : PPtr[PageSystemMenuButton]
	buttonParent : PPtr[Transform]
@UTTCGen
class HUDPage(MonoBehaviour):
	raycastBlocker : PPtr[Image]
	substackRectTransform : PPtr[RectTransform]
	dialogueButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	subStack : PPtr[object] # XXX: Fallback of PPtr<PageStack>
	charsheetNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	inventoryNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	journalNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	thcNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	mainMenuNavigateButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	moneyTimePortraitsBar : PPtr[RectTransform]
	backTapeBar : PPtr[RectTransform]
	quickAccessBar : PPtr[RectTransform]
	portraitsAnimator : PPtr[PageSystemHUDPortraitsAnimator]
	writersToolToggle : PPtr[object] # XXX: Fallback of PPtr<Button>
@UTTCGen
class StatsOverlayNavigationParameters(MonoBehaviour):
	isInventory : bool
@UTTCGen
class StatsOverlayPage(MonoBehaviour):
	background : PPtr[Image]
	backButton : PPtr[object] # XXX: Fallback of PPtr<Button>
	statsView : PPtr[StatsView]
	swipeDetector : PPtr[SwipeDetector]
