# Auto-generated by https://github.com/mos9527/UnityPyTypetreeCodegen
# Python definition for DiscoPages.Elements.MainMenu

from .... import *
from .... import ArchetypeAbility
from .... import ArchetypeButtonAnimatorHelper

@UTTCGen
class ArchetypeSelectionIndicator(MonoBehaviour):
	otherIndicatorPrefab : PPtr[GameObject]
	selectedIndicator : PPtr[GameObject]
	spacing : float
	transitionDuration : float
@UTTCGen
class ArchetypeSelectMenuButton(MonoBehaviour):
	isCustomCharacterButton : bool
	animatorHelper : PPtr[ArchetypeButtonAnimatorHelper]
	portrait : PPtr[Image]
	portraitHoverOverlay : PPtr[Image]
	signatureSkillLocalization : PPtr[object] # XXX: Fallback of PPtr<Localize>
	descriptionLocalization : PPtr[object] # XXX: Fallback of PPtr<Localize>
	nameLocalization : PPtr[object] # XXX: Fallback of PPtr<Localize>
	inte : PPtr[ArchetypeAbility]
	psy : PPtr[ArchetypeAbility]
	phq : PPtr[ArchetypeAbility]
	mot : PPtr[ArchetypeAbility]
	continueButton : PPtr[object] # XXX: Fallback of PPtr<Button>
@UTTCGen
class PageSystemAbilityPointsSet(MonoBehaviour):
	backgroundPoints : PPtr[object] # XXX: Fallback of PPtr<TMP_Text>
	pipsParent : PPtr[Transform]
	buttonIncrease : PPtr[object] # XXX: Fallback of PPtr<Button>
	buttonDecrease : PPtr[object] # XXX: Fallback of PPtr<Button>
@UTTCGen
class PageSystemMenuButton(MonoBehaviour):
	button : PPtr[object] # XXX: Fallback of PPtr<Button>
	text : PPtr[object] # XXX: Fallback of PPtr<TextMeshProUGUI>
	localization : PPtr[object] # XXX: Fallback of PPtr<Localize>
