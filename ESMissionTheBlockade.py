import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESShortcut as sc
import time

def run():
	print '--> mission The Blockade'

	# if not station.undock():
	# 	return False

	# if not space.warpToMissionLocation():
	# 	return False

	# if not space.enableAllLowSlot():
	# 	return False

	# if not space.openMissionDetail():
	# 	return False

	# if not space.openAfterBurn():
	# 	return False

	# if not space.launchDrones():
	# 	return False

	while not space.findV():
		if not space.findEnemy():
			dronesReturn()
			time.sleep(10)
			launchDrones()
			continue
		mouse.leftClick()
		key.keyPressEx(sc.Lock)
		# key.keyPressEx(sc.Keep)
		space.approach()
		time.sleep(8)
		space.fireOne()
		time.sleep(15)
		mouse.move(-200, 0)

	if not space.dronesReturn():
		return False

	if not space.missionObjectiveComplete():
		return False

	space.backToAgentStation()

	print '<-- mission The Blockade\n'
	return True
