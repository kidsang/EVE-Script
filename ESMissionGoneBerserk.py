import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot

def run():
	print '--> mission Gone Berserk'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.activateAccelerationGate():
		return False

	if not space.launchDrones():
		return False

	if not space.openMissionDetail():
		return False

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission Gone Berserk\n'
	return True
