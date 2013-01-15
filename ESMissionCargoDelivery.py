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
	print '--> mission Cargo delivery'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openAfterBurn():
		return False

	space.pickMissionItem()

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		mouse.leftClick()
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission Cargo delivery\n'
	return True
