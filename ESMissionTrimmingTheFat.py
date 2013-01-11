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

	if not space.enableAllLowSlot():
		return False

	if not space.launchDrones():
		return False

	if not space.openMissionDetail():
		return False

	# x = -1
	# while x < 0:
	# 	x, y = image.findImgR(panel.Full, 'img/close.bmp')
	# 	time.sleep(0.1)
	# mouse.moveTo(x, y)
	# mouse.leftClick()

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if not space.setMissionWaypoint():
		return False

	pilot.autopilot()

	print '<-- mission Trimming the Fat\n'
	return True
