import ImageGrab
import Image
import ImageEnhance
import ImageChops
import cv
import cv2
import pytesser.pytesser as tesser

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

def findImgR(rect, targetSource, threshould = 0.03):
    return findImg(rect[0], rect[1], rect[2], rect[3],
        targetSource, threshould)

def extractText(left, top, right, bottom, scale = 2):
    im = capture(left, top, right, bottom)
    im = im.resize([scale * i for i in im.size])
    return tesser.image_to_string(im)

def extractTextR(rect, scale = 2):
    return extractText(rect[0], rect[1], rect[2], rect[3], scale)

def test():
    pass

if __name__ == '__main__':
    test()