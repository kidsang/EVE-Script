import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot

def run():
	print '--> mission The Damsel In Distress'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openMissionDetail():
		return False

	if not space.lockTarget('img/pleasure_hub.bmp'):
		return False

	if not space.approach():
		return False

	if not space.openAfterBurn():
		return False

	if not space.launchDrones():
		return False

	if not space.fireOne():
		return False

	if not space.dronesEngage():
		return False

	#there are two cargos
	mouse.move(-200, 0)
	if not space.pickMissionItem():
		return False
	if not space.pickMissionItem():
		return False

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if not space.setMissionWaypoint():
		return False

	pilot.autopilot()


	print '<-- mission The Damsel In Distress\n'
	return True
