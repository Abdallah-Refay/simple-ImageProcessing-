import numpy
import cv2
import math
class pythontasks:
    def identity(self,image):
        row,col=numpy.shape(image)
        image2 = numpy.array(image)
        for r in range(row):
            for c in range(col):
                image[r][c] = image2[-r][c]
        return image

def identity():
      obj = pythontasks()
      img = cv2.imread('tele.png', 0)
      g = obj.identity(img)
      cv2.imshow('after', g)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

