import cv2
import os
from os import listdir
from os.path import isfile, join

img_folder = 'e:\\Dev\\datasets\\image-net\\n03492922\\images'

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('c:\\Users\\VIlyin\\Downloads\\output.avi', fourcc, 1.0, (640, 480))

images = [f for f in listdir(img_folder) if isfile(join(img_folder, f))]

for image in images:
    im = cv2.imread(os.path.join(img_folder, image))

    frame = cv2.resize(im, (640, 480), interpolation = cv2.INTER_CUBIC)
    out.write(frame)
    # cv2.imshow('frame', frame)
    # cv2.waitKey(0)

out.release()

a = ""