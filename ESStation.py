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
    x, y = image.findImgR(panel.MissionRight,
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
    mouse.leftClick()
    mouse.leftClick()

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
    time.wait(0.5)
    mouse.move(0, 50)

    print 'wait until accepting mission'
    while not findCompleteMission():
        time.sleep(0.2)

    if not findX():
        return False
    mouse.leftClick()

    print '<-- accept mission\n'

def test():
    startConversation('img/agent.bmp')

if __name__ == '__main__':
    test()