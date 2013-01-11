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
	print '--> mission Recon 3'

	if not station.undock():
		return False

	if not space.warpToMissionLocation():
		return False

	if not space.enableAllLowSlot():
		return False

	if not space.openMissionDetail():
		return False

	if not space.openAfterBurn():
		return False

	if not space.activateAccelerationGate():
		return False

	if not space.missionObjectiveComplete():
		return False

	if not space.backToAgentStation():
		return False

	print '<-- mission Recon 3\n'
	return True
