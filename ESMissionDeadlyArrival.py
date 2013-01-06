import ESMouse as mouse
import ESKeyboard as key
import ESImage as image
import ESStation as station
import ESSpace as space
import ESPilot as pilot
import ESPanel as panel

def run():
	print '--> mission Deadly Arrival'

	# if not station.undock():
	# 	return False

	# if not space.warpToMissionLocation():
	# 	return False

	# if not space.enableAllLowSlot():
	# 	return False


	# # in this mission we should approach a Large Collidable Object
	# x, y = image.findImgR(panel.Overview, 'img/overview.bmp')
	# if x < 0 or y < 0:
	# 	return False
	# mouse.moveTo(x, y)
	# mouse.leftClick()

	# x, y = image.findImgR(panel.Overview,
	# 	'img/load_lco.bmp')
	# if x < 0 or y < 0:
	# 	return False
	# mouse.moveTo(x, y)
	# mouse.leftClick()

	# if not space.lockTarget('img/ruined_structure.bmp'):
	# 	return False

	# if not space.approach():
	# 	return False

	# if not space.openAfterBurn():
	# 	return False

	# if not space.openMissionDetail():
	# 	return False

	# if not space.missionObjectiveComplete():
	# 	return False

	# # reset overview
	# x, y = image.findImgR(panel.Overview,
	# 	'img/overview.bmp')
	# if x < 0 or y < 0:
	# 	return False
	# mouse.moveTo(x, y)
	# mouse.leftClick()

	# x, y = image.findImgR(panel.Overview,
	# 	'img/load_kid.bmp')
	# if x < 0 or y < 0:
	# 	return False
	# mouse.moveTo(x, y)
	# mouse.leftClick()

	# if not space.backToAgentStation():
	# 	return False

	print '<-- mission Deadly Arrival\n'
	return True
