import numpy
import cv2

class pythontasks:
    def negative(self,image,k):
        row,col=numpy.shape(image)
        for r in range(row):
            for c in range(col):
                image [r][c]=255-image[r][c]
        return image

def negative():
    obj = pythontasks()
    img = cv2.imread('tele.png', 0)
    a = obj.negative(img, 5)
    cv2.imshow('after', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

