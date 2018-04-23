import numpy as np
from skimage import io
from skimage.color import rgb2hed, rgb2gray
from skimage.exposure import rescale_intensity

img_path = "e:\\Dev\\datasets\\gpn\\origin\\images00.09.48.000.jpeg"

img_rgb = io.imread(img_path)
img_hed = rgb2hed(img_rgb)

h = rescale_intensity(img_hed[:, :, 0], out_range=(0, 1))
d = rescale_intensity(img_hed[:, :, 2], out_range=(0, 1))

# grey image
io.imsave("e:\\images00.09.48.000_grey.jpeg", rgb2gray(img_rgb))

filter_1 = np.dstack((np.zeros_like(h), h, h))

io.imsave("e:\\images00.09.48.000_f4.jpeg", filter_1)