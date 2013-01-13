import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import ESPanel as panel
import time

def run():
	# print '--> mission Recon 1'

	if not station.undock():
		return False

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openMissionDetail():
		return False

	if not space.activateAccelerationGate():
		return False

	# pocket 1
	# can activate acceleration gate without cleaning
	mouse.move(-200, 0)

	if not space.openAfterBurn():
		return False

	if not space.activateAccelerationGate():
		return False

	# # pocket 2
	while not space.findOk():
		time.sleep(1)
	mouse.leftClick()
	
	if not space.missionObjectiveComplete():
		return False

	if not space.backToAgentStation():
		return False

	print '<-- mission Recon 1\n'
	return True
