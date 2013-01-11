import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission Unauthorized Military Presence'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.activateAccelerationGate():
		return False

	if not space.openMissionDetail():
		return False

	if not space.lockTarget('img/blood_raider_personnel.bmp'):
		return False

	if not space.openAfterBurn():
		return False

	if not space.approachFor(90):
		return False

	if not space.lockTarget('img/blood_raider_personnel.bmp'):
		return False

	if not space.launchDrones():
		return False

	if not space.fireOne():
		return False

	if not space.dronesEngage():
		return False

	# mission item is in wreck
	while space.findEnemy():
		mouse.leftClick()
		space.approach()
		key.keyPressEx(sc.Lock)
		time.sleep(8)
		space.fireOne()
		time.sleep(15)
		mouse.move(-200, 0)
		# collect
		space.pickWreck()

	if not space.dronesReturn():
		return False

	# pick wercks
	while space.pickWreck():
		pass
	mouse.leftUp()

	if not space.missionObjectiveComplete():
		return False

	if not space.setMissionWaypoint():
		return False

	pilot.autopilot()

	print '<-- mission Unauthorized Military Presence\n'
	return True
