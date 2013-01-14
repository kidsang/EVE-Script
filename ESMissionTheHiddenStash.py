import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot

def run():
	print '--> mission The Hidden Stash'

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

	if not space.lockTarget('img/warehouse.bmp'):
		return False

	if not space.openAfterBurn():
		return False

	if not space.approach():
		return False

	if not space.launchDrones():
		return False

	if not space.fireOne():
		return False

	if not space.dronesEngage():
		return False

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	# there are two cargos
	if not space.pickMissionItem():
		return False

	if not space.pickMissionItem():
		return False

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		mouse.leftClick()
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission The Hidden Stash\n'
	return True
