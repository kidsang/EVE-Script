import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission Seek And Destory'

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

	if not space.openAfterBurn():
		return False

	if not space.launchDrones():
		return False

	while space.findEnemy():
		mouse.leftClick()
		key.keyPressEx(sc.Lock)
		space.approach()
		time.sleep(8)
		space.fireOne()
		time.sleep(15)
		mouse.move(-200, 0)

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		space.exitStartMap()
		space.backToAgentStation()


	print '<-- mission Seek And Destory\n'
	return True
