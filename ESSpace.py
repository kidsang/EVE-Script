import ESPanel as panel
import ESImage as image
import ESMouse as mouse
import ESKeyboard as key
import ESShortcut as sc
import time
import random


def findRepairShop():
    x, y = image.findImgR(panel.StationServices,
        'img/repair_shop.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x + 20, y + 33)
        return True
    return False

def findAgentMission():
    x, y = image.findImgR(panel.Info,
        'img/agent_mission.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x + 20, y + 33)
        return True
    return False

def findInitializingMap():
    x, y = image.findImgR(panel.ProcessBar,
        'img/initializing_map.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findUndock():
    x, y = image.findImgR(panel.Menu, 
        'img/undock.bmp', 0.2)
    if x > 0 and y > 0:
        return True
    return False

def findSetDestination():
    x, y = image.findImgR(panel.Info,
        'img/set_destination.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findWarpToLocation():
    x, y = image.findImgR(panel.Info,
        'img/warp_to_location.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findReadDetail():
    x, y = image.findImgR(panel.Info,
        'img/read_details.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findDock():
    x, y = image.findImgR(panel.Info,
        'img/dock.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findO():
    x, y = image.findImgR(panel.MissionDetails,
        'img/o.bmp')
    if x != -1 and y != -1:
        return True
    return False

def findV():
    x, y = image.findImgR(panel.MissionDetails,
        'img/v.bmp')
    if x != -1 and y != -1:
        return True
    return False

def findX():
    x, y = image.findImgR(panel.MissionDetails,
        'img/x.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findClose():
    x, y = image.findImgR(panel.Full,
        'img/close.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findOK():
    x, y = image.findImgR(panel.Full,
        'img/ok.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findXFull():
    x, y = image.findImgR(panel.Full,
        'img/x.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findLootAll():
    x, y = image.findImgR(panel.Full,
        'img/loot_all.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findOpenCargo():
	x, y = image.findImgR(panel.SelectedItem,
		'img/open_cargo.bmp', 0.2)
	if x != -1 and y != -1:
		mouse.moveTo(x, y)
		return True
	return False

def findBig():
	x, y = image.findImgR(panel.Overview,
		'img/big.bmp', 0.2)
	if x != -1 and y != -1:
		mouse.moveTo(x, y)
		return True
	return False

def findSmall():
    x, y = image.findImgR(panel.Overview,
        'img/small.bmp', 0.2)
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findTarget(imgpath):
    x, y = image.findImgR(panel.Overview,
        imgpath)
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findEnemy():
    x, y = image.findColorR(panel.Overview, 'c11313')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False


def findCan():
    x, y = image.findImgR(panel.Overview,
        'img/can.bmp', 0.2)
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findDronesInBay():
    x, y = image.findImgR(panel.Drones,
        'img/bay.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findDronesInSpace():
    x, y = image.findImgR(panel.Drones,
        'img/local_space.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findIdle():
    x, y = image.findImgR(panel.Drones,
        'img/idle.bmp')
    if x != -1 and y != -1:
        return True
    return False

def findReturning():
    x, y = image.findImgR(panel.Drones,
        'img/returning.bmp')
    if x != -1 and y != -1:
        return True
    return False

def findFighting():
    x, y = image.findImgR(panel.Drones,
        'img/fighting.bmp')
    if x != -1 and y != -1:
        return True
	return False

def findLaunchDrones():
    x, y = image.findImgR(panel.Drones,
        'img/launch_drones.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findWarpDriveActive():
    x, y = image.findImgR(panel.DashBoard,
        'img/warp_drive_active.bmp', 0.3)
    if x != -1 and y != -1:
        return True
    return False

def findAccelerationGate():
    x, y = image.findImgR(panel.Overview,
        'img/acceleration_gate.bmp')
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
	mouse.leftClick()
	time.sleep(1)

	if not findSetDestination():
		return False
	mouse.leftClick()

	exitStartMap()

	print '<-- set mission waypoint\n'
	return True

def warpToMissionLocation():
	print '--> warp to mission location'

	enterStartMap()

	if not findAgentMission():
		return False
	mouse.leftClick()
	time.sleep(1)

	if not findWarpToLocation():
		return False
	mouse.leftClick()

	mouse.moveToP(panel.middle(panel.Message))
	mouse.leftDown()
	mouse.move(500, 200)
	mouse.leftUp()

	print 'wait until reach location'
	time.sleep(4)
	while findWarpDriveActive():
		time.sleep(0.1)

	exitStartMap()

	print '<-- warp to mission location\n'
	return True

def backToAgentStation():
	print '--> back to agent station'

	enterStartMap()

	if not findAgentMission():
		return False
	mouse.leftClick()
	time.sleep(1)

	if not findDock():
		return False
	mouse.leftClick()

	exitStartMap()

	print 'wait until reach station'
	while not findUndock():
		time.sleep(0.1)

	time.sleep(4)

	print '<-- back to agent station\n'
	return True


def enableAllLowSlot():
	print '--> enable low slot equipment'
	key.keyPressEx(sc.LowSlot1)
	key.keyPressEx(sc.LowSlot2)
	# key.keyPressEx(sc.LowSlot3)
	# key.keyPressEx(sc.LowSlot4)
	# key.keyPressEx(sc.LowSlot5)
	print '<-- enable low slot equipment\n'
	return True

def openAfterBurn():
	print '-->open after burn'
	key.keyPressEx(sc.MiddleSlot1)
	print '<--open after burn\n'
	return True

def lockBig():
	print '--> lock big'

	if not findBig():
		return False
	mouse.leftClick()
	key.keyPressEx(sc.Lock)
	mouse.move(-100, 0)
	time.sleep(3.5)
	print '<-- lock big\n'
	return True

def lockTarget(imgpath):
	target = imgpath.rfind('/')
	if target != -1:
		target = imgpath[target+1:]
	else:
		target = imgpath
	print '--> lock ' + target

	print 'finding target...'
	trycount = 0
	while not findTarget(imgpath):
		x, y = panel.middle(panel.Overview)
		y += random.random() * 40
		mouse.moveTo(x, y)
		mouse.leftClick()
		if trycount < 8:
			mouse.wheel(-12)
		elif trycount < 16:
			mouse.wheel(12)
		trycount += 1
		if trycount > 16:
			print 'can not find target'
			return False
	mouse.leftClick()
	key.keyPressEx(sc.Lock)
	time.sleep(3)

	print '<-- lock ' + target + '\n'
	return True

def fireOne():
	print '--> establishing hatred'
	key.keyPressEx(sc.HeightSlot1)
	time.sleep(1)
	key.keyPressEx(sc.HeightSlot1)
	print '<-- establishing hatred\n'
	return True

def approach():
	print '--> approaching target'
	key.keyPressEx(sc.Approach)
	print '<-- approaching target\n'
	return True

def approachFor(second):
	print '--> approaching target'

	key.keyPressEx(sc.Approach)

	while second > 0:
		time.sleep(1)
		second -= 1
		if second % 5 == 0:
			print str(second) + "second's left"

	print '<-- approaching target\n'
	return True

def pickMissionItem():
	print '--> picking mission item'

	print 'wait until cargo finded'
	trycount = 0
	while not findCan():
		x, y = panel.middle(panel.Overview)
		y += random.random() * 40
		mouse.moveTo(x, y)
		mouse.leftClick()
		if trycount < 8:
			mouse.wheel(-12)
		elif trycount < 16:
			mouse.wheel(12)
		trycount += 1
		if trycount >= 16:
			trycount = 0

	mouse.leftClick()
	key.keyPressEx(sc.Approach)

	if not findOpenCargo():
		return False
	mouse.leftClick()

	print 'wait until cargo open'
	while not findLootAll():
		time.sleep(0.1)
	mouse.leftClick()

	time.sleep(2)
	if not findXFull():
		return False
	mouse.leftClick()

	print '<-- picking mission item\n'
	return True

def pickWreck():
	print '--> picking wreck'

	if not findTarget('img/wreck.bmp'):
		return False
	mouse.leftClick()
	key.keyPressEx(sc.Approach)

	if not findOpenCargo():
		return False
	mouse.leftClick()

	print 'wait until cargo open'
	while not findLootAll():
		time.sleep(0.1)
	mouse.leftClick()

	time.sleep(2)
	if not findXFull():
		return False
	mouse.leftClick()

	print '<-- picking wreck\n'
	return True


def activateAccelerationGate():
	print '--> activate acceleration gate\n'

	enterStartMap()

	mouse.moveToP(panel.middle(panel.Message))
	mouse.leftDown()
	mouse.move(500, 200)
	mouse.leftUp()

	if not findAccelerationGate():
		return False
	mouse.leftClick()
	key.keyPressEx(sc.Activate)

	time.sleep(1)
	if findClose() or findOK():
		mouse.leftClick()
		mouse.move(0, -200)
	print 'wait to activate gate'
	while not findWarpDriveActive():
		time.sleep(0.1)
	time.sleep(4)
	if findClose() or findOK():
		mouse.leftClick()
		mouse.move(0, -200)
	print 'wait until reach location'
	while findWarpDriveActive():
		time.sleep(0.1)

	exitStartMap()

	print '<-- activate acceleration gate\n'
	return True

def launchDrones():
	print '--> lunch drones'

	if not findDronesInSpace():
		return False
	mouse.leftClick()

	if not findDronesInBay():
		return False
	mouse.rightClick()

	if not findLaunchDrones():
		return False
	mouse.leftClick()

	print 'wait until lunch drones'
	while not findIdle():
		time.sleep(0.1)

	print '<-- lunch drones\n'
	return True

def openMissionDetail():
	print '--> open mission detail'

	enterStartMap()

	if not findAgentMission():
		return False
	mouse.leftClick()
	time.sleep(1)

	if not findReadDetail():
		return False
	mouse.leftClick()

	print 'wait until find mission objective'
	while not findO():
		mouse.moveToP(panel.middle(panel.MissionDetails))
		mouse.leftClick()
		mouse.wheel(-20)

	exitStartMap()

	print '<-- open mission detail\n'
	return True

def missionObjectiveComplete():
	print '--> judge if mission complete'

	print 'wait until mission complete'
	while not findV():
		time.sleep(0.5)

	mouse.moveToP(panel.middle(panel.MissionDetails))
	time.sleep(0.5)
	if not findX():
		return False
	mouse.leftClick()

	print '<-- judge if mission complete\n'
	return True

def dronesEngage():
	print '--> drones engage'
	key.keyPressEx(sc.DronesEngage)
	key.keyPressEx(sc.DronesEngage)
	key.keyPressEx(sc.DronesEngage)
	print '<-- drones engage\n'
	return True

def dronesReturn():
	print '--> drones return'

	key.keyPressEx(sc.DronesReturn)
	key.keyPressEx(sc.DronesReturn)

	print 'wait until drones return'
	while findIdle() or findReturning() or findFighting():
		time.sleep(0.1)
		
	if not findDronesInSpace():
		return False
	mouse.leftClick()
	print '<-- drones return\n'
	return True

def repair():
	print '--> repair'
	x, y = image.findImgR(panel.StationServices, 'img/repair_shop.bmp')
	if x > 0:
		mouse.moveTo(x, y)
		mouse.leftClick()

	print 'wait until open repair facilities'
	x = -1
	while x < 0:
		x, y = image.findImgR(panel.Full, 'img/repair_facilities.bmp')
	mouse.moveTo(x, y + 70)
	mouse.leftClick()
	key.keyPressEx('ctrl+a')

	x, y = image.findImgR(panel.Full, 'img/repair_item.bmp')
	mouse.moveTo(x, y)
	mouse.leftClick()

	print 'wait..'
	x = -1
	while x < 0:
		x, y = image.findImgR(panel.Full, 'img/pick_new_item.bmp')

	x, y = image.findImgR(panel.Full, 'img/repair_all.bmp')
	if x > 0:
		mouse.moveTo(x, y)
		mouse.leftClick()
		print 'repairing..'
		x = -1
		while x < 0:
			x, y = image.findImgR(panel.Full, 'img/ok.bmp')
			if x < 0:
				return False
			mouse.moveTo(x, y)
			mouse.leftClick()
		x, y = image.findImgR(panel.Full, 'img/repair_facilities.bmp')
		mouse.moveTo(x, y)
	else:
		print 'nothing to repair'
	x, y = image.findImgR(panel.Full, 'img/x.bmp')
	mouse.moveTo(x, y)
	mouse.leftClick()


	print '<-- repair\n'
	return True

def test():
	mouse.moveTo(1000, 300)
	mouse.leftClick()
	repair()
	pass

if __name__ == '__main__':
	test()