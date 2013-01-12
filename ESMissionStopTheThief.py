import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission Stop The Thief'

	if not station.undock():
		return False

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.launchDrones():
		return False

	if not space.openMissionDetail():
		return False

	if not space.openAfterBurn():
		return False

	while space.findEnemy():
		mouse.leftClick()
		key.keyPressEx(sc.Lock)
		space.approach()
		time.sleep(8)
		space.fireOne()
		time.sleep(15)
		mouse.move(-200, 0)

	if not space.dronesReturn():
		return False

	space.pickMissionItem()

	if not space.missionObjectiveComplete():
		return False

	space.backToAgentStation()

	print '<-- mission Stop The Thief\n'
	return True
