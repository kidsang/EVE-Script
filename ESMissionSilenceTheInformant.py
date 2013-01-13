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
	print '--> mission Silence The Informant'

	# if not station.undock():
	# 	return False

	# pilot.autopilot() 

	# if not space.warpToMissionLocation():
	# 	return False

	# if not space.enableAllLowSlot():
	# 	return False

	# if not space.openMissionDetail():
	# 	return False

	# if not space.activateAccelerationGate():
	# 	return False

	# # # pocket 1
	# mouse.move(-200, 0)
	# if not space.findTarget("img/acceleration_gate.bmp"):
	# 	return False
	# mouse.leftClick()

	# if not space.approach():
	# 	return False

	# if not space.openAfterBurn():
	# 	return False

	# if not space.launchDrones():
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

	if not space.activateAccelerationGate():
		return False

	# pocket 2
		
	if not space.openAfterBurn():
		return False

	x = -1
	while x < 0:
		x, y = image.findImgR(panel.Full, 'img/close.bmp')
		time.sleep(0.1)
	mouse.moveTo(x, y)
	mouse.leftClick()
	time.sleep(1)

	if not space.launchDrones():
		return False

	while space.findEnemy():
		mouse.leftClick()
		space.approach()
		key.keyPressEx(sc.Lock)
		time.sleep(8)
		space.fireOne()
		time.sleep(15)
		mouse.move(-200, 0)

	if not space.dronesReturn():
		return False

	if not space.activateAccelerationGate():
		return False

	# pocket 3
	
	x = -1
	while x < 0:
		x, y = image.findImgR(panel.Full, 'img/close.bmp')
		time.sleep(0.1)
	mouse.moveTo(x, y)
	mouse.leftClick()
	time.sleep(1)	

	if not space.launchDrones():
		return False
		
	if not space.openAfterBurn():
		return False

	while space.findEnemy():
		mouse.leftClick()
		space.approach()
		key.keyPressEx(sc.Lock)
		time.sleep(8)
		space.fireOne()
		time.sleep(15)
		mouse.move(-200, 0)

	if not space.missionObjectiveComplete():
		return False

	if not space.dronesReturn():
		return False

	if not space.setMissionWaypoint():
		return False

	pilot.autopilot() 

	print '<-- mission Silence The Informant\n'
	return True
