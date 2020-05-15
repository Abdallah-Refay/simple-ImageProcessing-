
import numpy
import cv2
import math


class pythonTasks:


    def im2double(self,image):

        max_val=numpy.max(image)
        min_val=numpy.min(image)

        result=(image.astype('float')-min_val)/(max_val-min_val)
        return result

    def log(self,image,k):
      image=self.im2double(image)
      image=numpy.array(image)
      row,col=numpy.shape(image)

      for r in range(row):
            for c in range(col):
                image[r][c]=k*math.log(1+image[r][c],math.e)
      return image


def log():
    obj=pythonTasks()
    img=cv2.imread('tele.png',0)
    a=obj.im2double(img)
    cv2.imshow('after',a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()