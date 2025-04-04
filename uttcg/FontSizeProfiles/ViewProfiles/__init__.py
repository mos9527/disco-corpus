# Auto-generated by https://github.com/mos9527/UnityPyTypetreeCodegen
# Python definition for FontSizeProfiles.ViewProfiles

from ... import *
from ...FontSizeProfiles import AutoFontSizePerLanguage
from ...FontSizeProfiles.BuildParts import AutoTextElementSettings
from ...FontSizeProfiles import FontSizePerLanguage
from ...FontSizeProfiles.BuildParts import MonoBehaviourEnableSettings
from ...FontSizeProfiles.BuildParts import RectElementHeightSettings
from ...FontSizeProfiles.BuildParts import RectElementHorizontalSettings
from ...FontSizeProfiles.BuildParts import RectElementSettings
from ...FontSizeProfiles.BuildParts import TextElementSettings

@UTTCGen
class ArchetypeSelectionProfile(MonoBehaviour):
	ViewName : str
	archetypeSelection_Title : TextElementSettings
	archetypeSelection_Name : AutoTextElementSettings
	archetypeSelection_Description : AutoTextElementSettings
	archetypeSelection_StatName : TextElementSettings
	archetypeSelection_StatValue : TextElementSettings
	archetypeSelection_SignatureText : TextElementSettings
@UTTCGen
class CharsheetProfile(MonoBehaviour):
	ViewName : str
	attributeValue : TextElementSettings
	attributeName : TextElementSettings
	skillValue : TextElementSettings
	menuTitle : TextElementSettings
	overviewInfo : TextElementSettings
	highlightedSkillName : AutoTextElementSettings
	highlightedSkillDescription : AutoTextElementSettings
	highlightedSkillModifiers : TextElementSettings
	totalSkillPointsLabel : TextElementSettings
	totalSkillPointsValue : TextElementSettings
	experience : TextElementSettings
	skillPoints : TextElementSettings
	skillInfo : TextElementSettings
@UTTCGen
class CollageModeProfile(MonoBehaviour):
	ViewName : str
	subDrawerSelector : TextElementSettings
	title : AutoTextElementSettings
	button : TextElementSettings
	tooltip : TextElementSettings
	popup : TextElementSettings
	largeButton : TextElementSettings
	dialogueAutofill : AutoTextElementSettings
	screenshotPopup : TextElementSettings
@UTTCGen
class ControllerHelpMenuProfile(MonoBehaviour):
	ViewName : str
	controlerLabels : TextElementSettings
	controlerStadiaDisclaimer : TextElementSettings
@UTTCGen
class InfoPanelProfile(MonoBehaviour):
	ViewName : str
	title : TextElementSettings
	description : TextElementSettings
	tipsText : TextElementSettings
@UTTCGen
class InventoryProfile(MonoBehaviour):
	ViewName : str
	menuTitle : TextElementSettings
	equippedTitle : TextElementSettings
	equippedItemSlot : TextElementSettings
	autoItemName : AutoTextElementSettings
	itemEffect : TextElementSettings
	itemPrice : TextElementSettings
	itemDescription : TextElementSettings
	itemsTabLabels : TextElementSettings
	itemPawnShowClose : TextElementSettings
	tooltipTitle : TextElementSettings
	tooltipText : TextElementSettings
@UTTCGen
class JournalProfile(MonoBehaviour):
	ViewName : str
	screenTitle : TextElementSettings
	taskMapTab : TextElementSettings
	dayTitle : TextElementSettings
	taskItem : TextElementSettings
	activeDoneTab : TextElementSettings
	taskTitle : TextElementSettings
	taskState : TextElementSettings
	taskDetails : TextElementSettings
	officerProfile : TextElementSettings
	characterName : TextElementSettings
	characterRank : TextElementSettings
	characterStats : TextElementSettings
@UTTCGen
class LeftStatsHealthBonusesPanelProfile(MonoBehaviour):
	ViewName : str
	statNumericalValues : TextElementSettings
	statAbbreviation : TextElementSettings
	healthMoraleLabel : TextElementSettings
	healthMoraleValue : TextElementSettings
	bonusesTitle : TextElementSettings
	bonusesTextValues : TextElementSettings
	buttonPrompts : TextElementSettings
@UTTCGen
class MainMenuProfile(MonoBehaviour):
	ViewName : str
	mainMenuButtons : AutoTextElementSettings
@UTTCGen
class MapProfile(MonoBehaviour):
	ViewName : str
	checkTitle : AutoTextElementSettings
	checkDifficulty : TextElementSettings
	checkTutorial : AutoTextElementSettings
	characterName : TextElementSettings
@UTTCGen
class NewspaperEndingProfile(MonoBehaviour):
	ViewName : str
	headline : AutoTextElementSettings
	description : TextElementSettings
	paragraph : RectElementSettings
	backgroundCoverEnabled : MonoBehaviourEnableSettings
@UTTCGen
class OptionsProfile(MonoBehaviour):
	ViewName : str
	optionsLabels : TextElementSettings
	optionsItemsLabels : TextElementSettings
	optionsLanguageHelp : TextElementSettings
	optionsLanguageAnd : TextElementSettings
	optionElementHeight : RectElementHeightSettings
@UTTCGen
class SaveLoadProfile(MonoBehaviour):
	ViewName : str
	mainMenuButtons : TextElementSettings
	dateHourText : TextElementSettings
	dayRect : RectElementHorizontalSettings
	hourRect : RectElementHorizontalSettings
	saveName : RectElementHorizontalSettings
@UTTCGen
class ThoughtCabinetProfile(MonoBehaviour):
	ViewName : str
	menuTitle : TextElementSettings
	sortThoughts : TextElementSettings
	sortType : TextElementSettings
	thoughtListItem : TextElementSettings
	thoughtListItemAutoSize : AutoTextElementSettings
	thoughtTitle : TextElementSettings
	autoThoughtBonus : AutoTextElementSettings
	problemSolution : TextElementSettings
	description : TextElementSettings
	experiencePoints : TextElementSettings
	skillPointsLabel : TextElementSettings
@UTTCGen
class ThoughtSplashScreenProfile(MonoBehaviour):
	ViewName : str
	screenTitle : TextElementSettings
	thoughtTitle : AutoTextElementSettings
	description : TextElementSettings
	tabs : TextElementSettings
	stats : TextElementSettings
	button : TextElementSettings
@UTTCGen
class ViewProfile(MonoBehaviour):
	ViewName : str
