import win32api as api
from win32api import GetSystemMetrics
import win32con as con

def moveTo(x, y):
    winWidth = GetSystemMetrics(0)
    winHeight = GetSystemMetrics(1)
    absX = int(x * 65535.0 / winWidth)
    absY = int(y * 65535.0 / winHeight)
    api.mouse_event(con.MOUSEEVENTF_ABSOLUTE | con.MOUSEEVENTF_MOVE, absX, absY)

def move(dx, dy):
    api.mouse_event(con.MOUSEEVENTF_MOVE, dx, dy)

def leftDown():
    api.mouse_event(con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def leftUp():
    api.mouse_event(con.MOUSEEVENTF_LEFTUP, 0, 0)

def leftClick():
    leftDown()
    leftUp()

def rightDown():
    api.mouse_event(con.MOUSEEVENTF_RIGHTDOWN, 0, 0)

def rightUp():
    api.mouse_event(con.MOUSEEVENTF_RIGHTUP, 0, 0)

def rightClick():
    rightDown()
    rightUp()

def middleDown():
    api.mouse_event(con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)

def middleUp():
    api.mouse_event(con.MOUSEEVENTF_MIDDLEUP, 0, 0)

def middleClick():
    middleDown()
    middleUp()

def wheel(dz):
    """
    scroll up when dz > 0
    scroll down when dz < 0
    """
    api.mouse_event(con.MOUSEEVENTF_WHEEL, 0, 0, dz * con.WHEEL_DELTA)

def test():
    pass

if __name__ == '__main__':
    test()
