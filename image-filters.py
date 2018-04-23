import json
import numpy as np
from skimage.exposure import rescale_intensity
from skimage import io
from skimage.color import rgb2hed, rgb2gray
from skimage import util
import os
from os import listdir
from os.path import isfile, join
import shutil
import random
import copy

base_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images_wo_filters"
base_train_images_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images_wo_filters\\train"
base_val_images_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images_wo_filters\\val"
destination_base_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters"
destination_train_images_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\train"
destination_val_images_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\val"

with open(os.path.join(base_dir, "instances_train2014.json"), "r") as annotationsTrain:
    annotationsTrainData = json.load(annotationsTrain)

with open(os.path.join(base_dir, "instances_val2014.json"), "r") as annotationsVal:
    annotationsValData = json.load(annotationsVal)

newAnnotationsTrainData = copy.deepcopy(annotationsTrainData)

newAnnotationsValData = dict()
newAnnotationsValData["images"] = dict()
newAnnotationsValData["annotations"] = dict()


def get_max_id(dict, dict_key):
    max = 0

    for img in dict[dict_key]:
        if img["id"] > max:
            max = img["id"]

    return max


max_train_img_id = get_max_id(newAnnotationsTrainData, "images")
max_train_img_ann_id = get_max_id(newAnnotationsTrainData, "annotations")
max_val_img_id = 0
max_val_img_ann_id = 0


def increment_max_img_id():
    global max_train_img_id
    max_train_img_id += 1
    return max_train_img_id


def increment_max_img_ann_id():
    global max_train_img_ann_id
    max_train_img_ann_id += 1
    return max_train_img_ann_id


def get_destination_img_path(destination_images_dir, filter_number, filename, extension):
    return os.path.join(destination_images_dir, filename + "_f{}".format(str(filter_number)) + extension)


def copy_instance_annotations(img_entity, img_annotations, new_img_name, destination_dict):
    max_img_id = increment_max_img_id()

    img_entity = copy.deepcopy(img_entity)
    img_annotations = copy.deepcopy(img_annotations)

    img_entity["id"] = max_img_id
    img_entity["file_name"] = new_img_name

    destination_dict["images"].append(img_entity)

    for img_ann in img_annotations:
        max_img_ann_id = increment_max_img_ann_id()
        img_ann["id"] = max_img_ann_id
        img_ann["image_id"] = max_img_id
        destination_dict["annotations"].append(img_ann)


def get_img_annotations(img_name, annotations):
    for img in annotations["images"]:
        if img["file_name"] == img_name:
            img_entity = img
            break

    img_annotations = []
    for ann in annotations["annotations"]:
        if ann["image_id"] == img_entity["id"]:
            img_annotations.append(ann)

    return copy.deepcopy(img_entity), copy.deepcopy(img_annotations)


def add_filters_to_img(destination_images_dir, img_path, img_name, annotations, destination_dict):
    base, extension = os.path.splitext(img_name)

    img_rgb = io.imread(img_path)
    img_hed = rgb2hed(img_rgb)

    f1_filepath = get_destination_img_path(destination_images_dir, 1, base, extension)
    io.imsave(f1_filepath, rgb2gray(img_rgb))

    img_entity, img_annotations = get_img_annotations(img_name, annotations)

    copy_instance_annotations(img_entity, img_annotations, base + "_f1" + extension, destination_dict)

    # Rescale hematoxylin and DAB signals and give them a fluorescence look
    h = rescale_intensity(img_hed[:, :, 0], out_range=(0, 1))
    d = rescale_intensity(img_hed[:, :, 2], out_range=(0, 1))

    zdh = np.dstack((np.zeros_like(h), d, h))
    f2_filepath = get_destination_img_path(destination_images_dir, 2, base, extension)
    io.imsave(f2_filepath, zdh)

    copy_instance_annotations(img_entity, img_annotations, base + "_f2" + extension, destination_dict)

    zdh = np.dstack((np.zeros_like(h), d, d))
    f3_filepath = get_destination_img_path(destination_images_dir, 3, base, extension)
    io.imsave(f3_filepath, zdh)

    copy_instance_annotations(img_entity, img_annotations, base + "_f3" + extension, destination_dict)

    zdh = np.dstack((np.zeros_like(h), h, h))
    f4_filepath = get_destination_img_path(destination_images_dir, 4, base, extension)
    io.imsave(f4_filepath, zdh)

    copy_instance_annotations(img_entity, img_annotations, base + "_f4" + extension, destination_dict)

    f5_filepath = get_destination_img_path(destination_images_dir, 5, base, extension)
    io.imsave(f5_filepath, util.random_noise(img_rgb[:,:,:3], mode="salt", amount=random.uniform(0.05, 0.15)))

    copy_instance_annotations(img_entity, img_annotations, base + "_f5" + extension, destination_dict)


train_images = [f for f in listdir(base_train_images_dir) if isfile(join(base_train_images_dir, f))]

for img in train_images:
    shutil.copy(os.path.join(base_train_images_dir, img), os.path.join(destination_train_images_dir, img))
    add_filters_to_img(destination_train_images_dir, os.path.join(base_train_images_dir, img), img, annotationsTrainData, newAnnotationsTrainData)

with open(os.path.join(destination_base_dir, "instances_train2014.json"), "w+") as annTrainWithFilters:
    json.dump(newAnnotationsTrainData, annTrainWithFilters)

for img in annotationsValData["images"]:
    increment_max_img_id()

    for ann in annotationsValData["annotations"]:
        if ann["image_id"] == img["id"]:
            ann["image_id"] = max_train_img_id
            increment_max_img_ann_id()
            ann["id"] = max_train_img_ann_id

    img["id"] = max_train_img_id

newAnnotationsValData = copy.deepcopy(annotationsValData)

val_images = [f for f in listdir(base_val_images_dir) if isfile(join(base_val_images_dir, f))]

for img in val_images:
    shutil.copy(os.path.join(base_val_images_dir, img), os.path.join(destination_val_images_dir, img))
    add_filters_to_img(destination_val_images_dir, os.path.join(base_val_images_dir, img), img, annotationsValData, newAnnotationsValData)

with open(os.path.join(destination_base_dir, "instances_val2014.json"), "w+") as annValWithFilters:
    json.dump(newAnnotationsValData, annValWithFilters)

