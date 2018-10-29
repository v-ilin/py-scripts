import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

base_path = 'c:\\Users\\VIlyin\\Downloads\\quality-of-gpn-images'

images_names = ['images03.00.09.000.jpeg',
                '00.00.47.000.jpg',
                '00.01.02.000.jpg',
                'images02.59.45.000.jpeg',
                'images02.59.45.000_f1.jpg',
                'images02.59.45.000_f2.jpg']

# image_name = '00.00.47.000.jpg'
image_name = 'images02.59.45.000_f1.jpg'
# image_name = 'images02.59.45.000_f2.jpg'
# image_name = 'belt_01.55.50.000.jpg'
# image_name = 'belt_01.58.00.000.jpg'

# bbox_x_min = 1
# bbox_y_min = 1
# bbox_x_max = 754
# bbox_y_max = 1200

bbox_x_min = 44
bbox_y_min = 1
bbox_x_max = 692
bbox_y_max = 1200


def get_laplacian_variance(img):
    image_with_laplacian_filter = cv2.Laplacian(img, cv2.CV_64F)
    return image_with_laplacian_filter, image_with_laplacian_filter.var()


def show_image(img):
    window_name = 'image'

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, img.shape[1], img.shape[0])
    cv2.imshow(window_name, img, )
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_bbox_from_image(img, x_min, y_min, x_max, y_max):
    return img[y_min:y_max, x_min:x_max]


def get_image_brightness(img):
    return np.mean(img)


image_path = os.path.join(base_path, image_name)
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image not found: {}'.format(img))
else:
    image_bbox = get_bbox_from_image(img, bbox_x_min, bbox_y_min, bbox_x_max, bbox_y_max)

    show_image(image_bbox)

    image_brightness = get_image_brightness(img)
    image_bbox_brightness = get_image_brightness(image_bbox)

    image_with_laplacian_filter, image_variance_of_laplacian = get_laplacian_variance(img)
    image_bbox_with_laplacian_filter, image_bbox_variance_of_laplacian = get_laplacian_variance(image_bbox)

    show_image(image_with_laplacian_filter)
    show_image(image_bbox_with_laplacian_filter)

    figure = plt.figure(num=image_name)
    figure.text(0.2, 0.8, 'Variance of Laplacian = {}'.format(image_variance_of_laplacian))

    plt.hist(img.ravel(),256,[0,256])
    plt.plot(image_variance_of_laplacian)
    plt.title(image_name)

    plt.ion()
    plt.show()

d = ''