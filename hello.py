import cv2 as cv

img = cv.imread('\cv_pics\cat2.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)