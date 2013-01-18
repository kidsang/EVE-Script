import time
import ESKeyboard as key
import ESMouse as mouse
import ESImage as image
import ESPanel as panel
import ESShortcut as sc

def findTargetStarGate():
    x, y = image.findImgR(panel.Overview,
       'img/target_star_gate.bmp', 0.2)
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False

def findTargetStation():
    x, y = image.findImgR(panel.Overview,
       'img/target_station.bmp', 0.2)
    if x != -1 and y != -1:
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

def findEnteringStation():
    x, y = image.findImgR(panel.ProcessBar,
        'img/entering_station.bmp')
    if x != -1 and y != -1:
        mouse.moveTo(x, y)
        return True
    return False


def jump():
    mouse.leftClick()
    key.keyPressEx(sc.Warp)
    time.sleep(1)
    key.keyPressEx(sc.Activate)

def dock():
    mouse.leftClick()
    key.keyPressEx(sc.Activate)

def autopilot():
    print '--> autopilot'

    arrived = False
    while not arrived:
        print 'try to find target stargate or station'
        finded = ''
        for retry in range(7):
            mouse.moveToP(panel.middle(panel.Full))
            print 'try: ' + str(retry + 1)
            if findTargetStation():
                finded = 'station'
                break
            elif findTargetStarGate():
                finded = 'stargate'
                break
            else:
                mouse.moveToP(panel.middle(panel.Overview))
                mouse.leftClick()
                mouse.wheel(-12)

        if finded == '':
            print "can't find any waypoint"
            arrived = True
            break

        if finded == 'station':
            print 'target station finded, dock'
            dock()
            print 'wait until entering station'
            while not findEnteringStation():
                time.sleep(0.1)
            print 'entering station'
            time.sleep(4)
            arrived = True
            break

        if finded == 'stargate':
            print 'target stargate finded, jump'
            jump()
            print 'wait until entering space'
            while not findEnteringSpace():
                time.sleep(0.1)
            print 'entering space'
            time.sleep(4)

    time.sleep(1)
    print '<-- autopilot\n'





# x, y = image.findImg(300, 300, 1000, 1000, 'img/test3.bmp')
# if x != -1 and y != -1:
#     mouse.moveTo(x, y)
# print x, y

def test():
    autopilot()

if __name__ == '__main__':
    test()
