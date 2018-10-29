from roipoly import roipoly
import pylab as pl
import numpy as np

image = pl.imread("e:/gpn/danger_zone.jpg")
image_arr = np.asarray(image)
pl.imshow(image)
MyROI = roipoly(roicolor='r') # draw new ROI in red color
mask = MyROI.getMask(image_arr[:2,:2])
pl.imshow(mask)