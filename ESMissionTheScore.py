import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESPanel as panel
import time
import ESShortcut as sc

def run():
	print '--> mission Eliminate the Score'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openMissionDetail():
		return False

	if not space.activateAccelerationGate():
		return False

	if not space.launchDrones():
		return False

	while not space.findV():
		if space.findEnemy():
			mouse.leftClick()
			key.keyPressEx(sc.Lock)
			time.sleep(10)
			space.fireOne()
			time.sleep(10)

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		mouse.leftClick()
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission Eliminate the Score\n'
	return True
