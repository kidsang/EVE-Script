import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time
import ESPanel as panel

def run():
	print '--> mission Foreign Investment'

	# if not station.undock():
	# 	return False

	# if not space.warpToMissionLocation():
	# 	return False

	# if not space.enableAllLowSlot():
	# 	return False

	# # there are guards
	# if not space.launchDrones():
	# 	return False

	# if not space.openMissionDetail():
	# 	return False

	# if not space.openAfterBurn():
	# 	return False

	# while space.findEnemy():
	# 	mouse.leftClick()
	# 	key.keyPressEx(sc.Lock)
	# 	time.sleep(8)
	# 	space.fireOne()
	# 	time.sleep(15)
	# 	mouse.move(-200, 0)

	# if not space.dronesReturn():
	# 	return False

	# if not space.findTarget("img/acceleration_gate.bmp"):
	# 	return False
	# mouse.leftClick()
	# key.keyPressEx(sc.Activate)

	# space.enterStartMap()
	# mouse.moveToP(panel.middle(panel.Message))
	# mouse.leftDown()
	# mouse.move(500, 200)
	# mouse.leftUp()

	# print 'wait until activate gate'
	# while not space.findWarpDriveActive():
	# 	time.sleep(0.1)
	# print 'wait until reach location'
	# while space.findWarpDriveActive():
	# 	time.sleep(0.1)

	# space.exitStartMap()

	# # pocket 1
	# mouse.move(-200, 0)
	# if not space.lockTarget("img/gallente_company_hq.bmp"):
	# 	return False

	# if not space.approach():
	# 	return False

	# if not space.launchDrones():
	# 	return False

	# if not space.fireOne():
	# 	return False

	# if not space.missionObjectiveComplete():
	# 	return False

	# if not space.dronesReturn():
	# 	return False

	# if not space.backToAgentStation():
	# 	return False

	print '<-- mission Foreign Investment\n'
	return True
