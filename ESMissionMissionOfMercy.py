import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission Mission of Mercy'

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

	# wait for enemy to warp in
	time.sleep(60)

	# establish hate
	if space.findEnemy():
		mouse.leftClick()
		key.keyPressEx(sc.Lock)
		space.approach()
		time.sleep(10)
		space.fireOne()
		time.sleep(6)

	if not space.launchDrones():
		return False

	while not space.findV() and space.findEnemy():
		mouse.leftClick()
		key.keyPressEx(sc.Keep)
		key.keyPressEx(sc.Lock)
		time.sleep(10)
		space.fireOne()
		time.sleep(8)
		mouse.move(-200, 0)
		mouse.leftClick()

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

	print '<-- mission Mission of Mercy\n'
	return True
