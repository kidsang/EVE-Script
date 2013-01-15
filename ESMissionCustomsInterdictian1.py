import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESPanel as panel
import time

def run():
	print '--> mission Customs lnterdictian (1 of 2)'

	if not station.undock():
		return False

	pilot.autopilot()

	space.warpToMissionLocation()

	#this mission don't have a acceleration gate
	#and will pop up a dialog
	time.sleep(10)
	if space.findClose():
		mouse.leftClick()

	if not space.enableAllLowSlot():
		return False

	if not space.openMissionDetail():
		return False

	if not space.lockBig():
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

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if not space.pickMissionItem():
		return False

	if not space.setMissionWaypoint():
		return False

	pilot.autopilot()

	print '<-- mission Customs lnterdictian (1 of 2)\n'
	return True
