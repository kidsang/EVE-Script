import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import ESPanel as panel

def run():
	print '--> mission Technological Secrets (3 of 3)'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.launchDrones():
		return False

	if not space.openMissionDetail():
		return False

	while not space.findV():
		# collect
		space.pickWreck()

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
		
	print '<-- mission Technological Secrets (3 of 3)\n'
	return True
