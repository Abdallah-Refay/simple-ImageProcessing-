import numpy
import cv2

class pythontasks:
    def intensity(self,image):
        row,col=numpy.shape(image)
        min=10
        max=100
        for r in range(row):
            for c in range(col):
                if image[r][c]>min and image[r][c]<max:
                    image[r][c]=255
                else:
                    image[r][c]=1
        return image
def intensity():
    obj=pythontasks()
    img=cv2.imread('tele.png',0)
    a=obj.intensity(img)
    cv2.imshow('intensity',a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()