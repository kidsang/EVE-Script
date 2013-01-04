import win32api as api
from win32api import GetSystemMetrics
import win32con as con
import time

cd = 0.5

def moveTo(x, y):
    winWidth = GetSystemMetrics(0)
    winHeight = GetSystemMetrics(1)
    absX = int(x * 65535.0 / winWidth)
    absY = int(y * 65535.0 / winHeight)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)
    time.sleep(cd)

def moveToP(point):
    moveTo(point[0], point[1])

def move(dx, dy):
    api.mouse_event(con.MOUSEEVENTF_MOVE, dx, dy)
    time.sleep(cd)

def moveP(point):
    move(point[0], point[1])

def leftDown():
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(cd)

def leftUp():
    api.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def leftClick():
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(cd)

def rightDown():
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(cd)

def rightUp():
    api.mouse_event(con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(cd)

def rightClick():
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(cd)

def middleDown():
    api.mouse_event(con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    time.sleep(cd)

def middleUp():
    api.mouse_event(con.MOUSEEVENTF_MIDDLEUP, 0, 0)
    time.sleep(cd)

def middleClick():
    api.mouse_event(con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    api.mouse_event(con.MOUSEEVENTF_MIDDLEUP, 0, 0)
    time.sleep(cd)

def wheel(dz):
    """
    scroll up when dz > 0
    scroll down when dz < 0
    """
    api.mouse_event(con.MOUSEEVENTF_WHEEL, 0, 0, dz * con.WHEEL_DELTA)
    time.sleep(cd)

def test():
    pass

if __name__ == '__main__':
    test()
