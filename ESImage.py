import ImageGrab
import cv
import cv2

def capture(left, top, right, bottom):
    img = ImageGrab.grab((left, top, right, bottom))
    return img

def findImg(left, top, right, bottom, targetSource, threshould = 0.03):
    '''
    left, top, right, bottom: the region you want to search
    targetSource: target bitmap file path
    threshould: range from 0.0 to 1.0,
                smaller threshould means more accurate
    '''
    temppath = 'img/temp.bmp'
    img = capture(left, top, right, bottom)
    img.save(temppath)
    source = cv2.imread(temppath)
    target = cv2.imread(targetSource)
    result = cv2.matchTemplate(source, target, cv.CV_TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if minVal <= threshould:
        return (minLoc[0] + left, minLoc[1] + top)
    else:
        return (-1, -1)



def test():
    pass

if __name__ == '__main__':
    test()