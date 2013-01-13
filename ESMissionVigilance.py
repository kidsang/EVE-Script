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
	print '--> mission Vigilance'

	if not station.undock():
		return False

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openAfterBurn():
		return False

	while not space.lockTarget('img/suspicious.bmp'):
		time.sleep(5)

	if not space.launchDrones():
		return False

	if not space.dronesEngage():
		return False

	if not space.pickMissionItem():
		return False

	if not space.dronesReturn():
		return False

	if not space.backToAgentStation():
		return False

	print '<-- mission Vigilance\n'
	return True
