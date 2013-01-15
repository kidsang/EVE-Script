import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESPanel as panel
import time

def run():
	print '--> mission Saving A Mans Career'

	if not station.undock():
		return False

	pilot.autopilot()

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if space.findClose():
		mouse.leftClick()

	if not space.lockTarget('img/sangrel_minn.bmp'):
		return False

	space.openAfterBurn()

	space.approachFor(30)

	if not space.launchDrones():
		return False

	space.fireOne()

	space.dronesEngage()

	if not space.pickMissionItem():
		return False

	if not space.dronesReturn():
		return False

	if space.setMissionWaypoint():
		pilot.autopilot()
	else:
		mouse.leftClick()
		space.exitStartMap()
		space.backToAgentStation()

	print '<-- mission Saving A Mans Career\n'
	return True
