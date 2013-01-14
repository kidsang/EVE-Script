import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission Smuggler Interception'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
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
		space.pickWreck()

	if not space.dronesReturn():
		return False

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission Smuggler Interception\n'
	return True
