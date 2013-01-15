import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESPanel as panel
import time

def run():
	print '--> mission Trimming the Fat'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	print 'wait for message show up'
	time.sleep(8)
	if space.findClose():
		mouse.leftClick()

	if not space.enableAllLowSlot():
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
		mouse.leftClick()
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission Trimming the Fat\n'
	return True
