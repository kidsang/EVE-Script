import ESPanel as panel
import ESImage as image
import ESMouse as mouse
import ESKeyboard as key
import time

def findUndock():
    x, y = image.findImgR(panel.Menu, 
        'img/undock.bmp', 0.2)
    if x > 0 and y > 0:
        mouse.moveTo(x, y)
        return True
    return False

def findEnteringSpace():
    x, y = image.findImgR(panel.ProcessBar,
        'img/entering_space.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findAgent(agentPicSource):
    x, y = image.findImgR(panel.StationServices,
        agentPicSource)
    if x != -1 and y != -1:
        mouse.moveTo(x + 10, y + 10)
        return True
    return False

def findInfo():
    x, y = image.findImgR(panel.MissionLeft,
        'img/info.bmp')
    if x != -1 and y != -1:
        return True
    return False

def findAccept():
    x, y = image.findImgR(panel.MissionRight,
        'img/accept.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findX():
    x, y = image.findImgR(panel.Mission,
        'img/x.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findCompleteMission():
    x, y = image.findImgR(panel.MissionRight,
        'img/complete_mission.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findRequestMission():
    x, y = image.findImgR(panel.Mission,
        'img/request_mission.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False


def undock():
    print '--> undock'

    if not findUndock():
        return False

    mouse.leftClick()
    mouse.move(200, 0)

    print 'wait until undock'
    while findUndock():
        time.sleep(0.1)

    print 'wait until entering space'
    while not findEnteringSpace():
        time.sleep(0.1)

    time.sleep(3)

    print '<-- undock\n'
    return True

def startConversation(agentPicSource):
    print '--> start conversation'

    if not findAgent(agentPicSource):
        return False
    mouse.doubleClick()

    print 'wait until conversation start'
    while not findInfo():
        time.sleep(0.1)

    print '<-- start conversation\n'
    return True

def acceptMission():
    print '--> accept mission'

    if not findAccept():
        return False
    mouse.leftClick()
    mouse.move(0, 50)

    print 'wait until accepting mission'
    while not findCompleteMission():
        time.sleep(0.2)

    if not findX():
        return False
    mouse.leftClick()

    print '<-- accept mission\n'
    return True

def declineMission():
    print '--> decline mission'

    x, y = image.findImgR(panel.MissionRight, 'img/decline.bmp')
    mouse.moveTo(x, y)
    mouse.leftClick()

    time.sleep(5)
    x, y = image.findImgR(panel.Full, 'img/yes.bmp')
    if x > 0:
        mouse.moveTo(x, y)
        mouse.leftClick()

    print 'wait until decline'

    while not findRequestMission():
        time.sleep(0.5)
    mouse.leftClick()

    while not findX():
        time.sleep(0.2)
    mouse.leftClick()

    time.sleep(1)

    print '<-- decline mission\n'
    return True

def completeMission():
    print '--> complete mission\n'

    if not findCompleteMission():
        return False
    mouse.leftClick()

    print 'wait until complete mission'
    while not findRequestMission():
        time.sleep(0.1)

    if not findX():
        return False
    mouse.leftClick()

    print '<-- complete mission\n'
    return True

def openInventory():
    print '--> open inventory'

    x, y = image.findImgR(panel.Menu, 'img/inventory.bmp', 0.2)
    if x < 0:
        return False
    mouse.moveTo(x, y)
    mouse.leftClick()
    time.sleep(1)

    print '<-- open inventory\n'
    return True

def closeInventory():
    print '--> close inventory'

    mouse.moveToP(panel.middle(panel.Inventory))
    x, y = image.findImgR(panel.Inventory, 'img/x.bmp')
    if x < 0:
        return False
    mouse.moveTo(x, y)
    mouse.leftClick()
    time.sleep(1)
    
    print '<-- close inventory\n'
    return True

def loadItem(item):
    print '--> load item ' + item

    x, y = image.findImgR(panel.Inventory, 'img/item_hangar.bmp', 0.2)
    if x > 0:
        mouse.moveTo(x, y)
        mouse.leftClick()
        time.sleep(1.5)

    x = -1
    x, y = image.findImgR(panel.Inventory, item)
    while x < 0:
        mouse.moveToP(panel.middle(panel.Inventory))
        mouse.leftClick()
        mouse.wheel(-12)
        mouse.move(300, 0)
        x, y = image.findImgR(panel.Inventory, item)

    mouse.moveTo(x, y)
    mouse.leftDown()
    x, y = image.findImgR(panel.Inventory, 'img/ship.bmp', 0.2)
    if x < 0:
        mouse.leftUp()
        return False
    mouse.moveTo(x, y)
    mouse.leftUp()
    time.sleep(1)

    print '<-- load item ' + item + '\n'
    return True

def unloadItem(item):
    print '--> unload item ' + item

    x, y = image.findImgR(panel.Inventory, 'img/ship.bmp', 0.2)
    if x > 0:
        mouse.moveTo(x, y)
        mouse.leftClick()
        time.sleep(1.5)

    x = -1
    x, y = image.findImgR(panel.Inventory, item)
    while x < 0:
        mouse.moveToP(panel.middle(panel.Inventory))
        mouse.leftClick()
        mouse.wheel(-12)
        mouse.move(300, 0)
        x, y = image.findImgR(panel.Inventory, item)

    mouse.moveTo(x, y)
    mouse.leftDown()
    x, y = image.findImgR(panel.Inventory, 'img/item_hangar.bmp', 0.2)
    if x < 0:
        mouse.leftUp()
        return False
    mouse.moveTo(x, y)
    mouse.leftUp()
    time.sleep(1)

    print '<-- unload item ' + item + '\n'
    return True

def test():
    # openInventory()
    # loadItem('img/dna_sample.bmp')
    # unloadItem('img/dna_sample.bmp')
    # closeInventory()
    pass

if __name__ == '__main__':
    test()