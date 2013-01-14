import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission The Blockade'

	if not station.undock():
		return False

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openMissionDetail():
		return False

	if not space.launchDrones():
		return False

	while not space.findV():
		if space.lockTarget('img/enslaver') or space.lockTarget('img/plague'):
			space.dronesReturn()
			time.sleep(8)
			space.launchDrones()
			space.fireOne()
			space.dronesEngage()
			time.sleep(20)
		else:
			time.sleep(5)

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	space.backToAgentStation()

	print '<-- mission The Blockade\n'
	return True
