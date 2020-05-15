import numpy
import cv2
import math
class pythonTasks:


    def double (self,image):

        max_val=numpy.max(image)
        min_val=numpy.min(image)

        val=(image.astype('float')-min_val)/(max_val-min_val)
        return val



    def power_law(self, image, y, ):
        image=self.double(image)
        row,col=numpy.shape(image)
        for r in range (row):
            for c in range (col):
                image[r][c]=2*math.pow(image[r][c],y)
        return image


def powerlow():
    obj=pythonTasks()
    i=cv2.imread('tele.png',0)
    a=obj.power_law(i,0.9)
    cv2.imshow('after',a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
