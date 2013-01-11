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
	print '--> mission Recon 1'

	# if not station.undock():
	# 	return False

	# if not space.warpToMissionLocation():
	# 	return False

	# if not space.enableAllLowSlot():
	# 	return False

	# if not space.openMissionDetail():
	# 	return False

	# if not space.activateAccelerationGate():
	# 	return False

	# # pocket 1
	# # can activate acceleration gate without cleaning
	# mouse.move(-200, 0)
	# if not space.findTarget("img/acceleration_gate.bmp"):
	# 	return False
	# mouse.leftClick()

	# if not space.approach():
	# 	return False

	# if not space.openAfterBurn():
	# 	return False

	# key.keyPressEx(sc.Activate)

	# space.enterStartMap()

	# mouse.moveToP(panel.middle(panel.Message))
	# mouse.leftDown()
	# mouse.move(500, 200)
	# mouse.leftUp()

	# print 'wait to activate acceleration gate'
	# while not space.findWarpDriveActive():
	# 	time.sleep(0.1)
	# print 'wait until reach location'
	# while space.findWarpDriveActive():
	# 	time.sleep(0.1)

	# # # pocket 2
	# # a dialog will show up
	# x = -1
	# y = -1
	# while x < 0 or y < 0:
	# 	x, y = image.findImgR('img/ok.bmp', panel.Full)
	# 	time.sleep(0.1)
	# mouse.moveTo(x, y)
	# mouse.leftClick()
	# time.sleep(1)

	# if not space.missionObjectiveComplete():
	# 	return False

	# if not space.dronesReturn():
	# 	return False

	# if not space.backToAgentStation():
	# 	return False

	print '<-- mission Recon 1\n'
	return True
