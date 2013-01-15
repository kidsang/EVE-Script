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
	print '--> mission Silence The Informant'

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

	print 'pocket 1'

	if not space.openAfterBurn():
		return False

	if not space.launchDrones():
		return False

	while space.findEnemy():
		mouse.leftClick()
		key.keyPressEx(sc.Lock)
		space.approach()
		time.sleep(10)
		space.fireOne()
		time.sleep(10)
		mouse.move(-200, 0)

	if not space.dronesReturn():
		return False

	if not space.activateAccelerationGate():
		return False

	print 'pocket 2'
	time.sleep(5)
	if space.findClose():
		mouse.leftClick()

	if not space.launchDrones():
		return False

	if not space.openAfterBurn():
		return False

	while space.findEnemy():
		mouse.leftClick()
		key.keyPressEx(sc.Lock)
		space.approach()
		time.sleep(10)
		space.fireOne()
		time.sleep(10)
		mouse.move(-200, 0)

	if not space.dronesReturn():
		return False

	if not space.activateAccelerationGate():
		return False

	print 'pocket 3'
	time.sleep(5)
	if space.findClose():
		mouse.leftClick()

	if not space.launchDrones():
		return False
		
	if not space.openAfterBurn():
		return False

	while space.findEnemy():
		mouse.leftClick()
		space.approach()
		key.keyPressEx(sc.Lock)
		time.sleep(10)
		space.fireOne()
		time.sleep(10)
		mouse.move(-200, 0)

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

	print '<-- mission Silence The Informant\n'
	return True
