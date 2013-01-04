import ESPanel as panel
import ESImage as image
import ESMouse as mouse
import ESKeyboard as key
import ESShortcut as sc
import time


def findAgentMission():
    x, y = image.findImgR(panel.Info,
        'img/agent_mission.bmp', 0.2)
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findInitializingMap():
    x, y = image.findImgR(panel.ProcessBar,
        'img/initializing_map.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findSetDestination():
    x, y = image.findImgR(panel.Info,
        'img/set_destination.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def enterStartMap():
	print '--> enter start map'

	key.keyPressEx(sc.Map)
	time.sleep(3)

	print '<-- enter start map\n'

def exitStartMap():
	print '--> exit start map'
	key.keyPressEx(sc.Map)
	time.sleep(2)
	print '<-- exit start map\n'


def setMissionWaypoint():
	print '--> set mission waypoint'

	enterStartMap()

	if not findAgentMission():
		return False
	mouse.move(33, 30)
	mouse.leftClick()
	time.sleep(1)

	if not findSetDestination():
		return False
	mouse.leftClick()

	exitStartMap()

	print '<-- set mission waypoint\n'
	return True

def test():
	# setMissionWaypoint()
	pass

if __name__ == '__main__':
	test()