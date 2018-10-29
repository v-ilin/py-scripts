import os
from os import listdir
from os.path import isfile, join
import shutil

images_dir = "e:\\dev\\datasets\\ann_results\\ann_results_3 (belt)\\separated\\val\\images"
annotations_dir = "e:\\dev\\datasets\\ann_results\\ann_results_3 (belt)\\separated\\val\\annotations"

files = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]

images_without_annotations = []

for i, filename in enumerate(files):
    name, extension = os.path.splitext(filename)

    if not os.path.exists(os.path.join(annotations_dir, name + ".xml")):
        print(filename)
        images_without_annotations.append(filename)

# for img in images_without_annotations:
#     os.remove(os.path.join(images_dir, img))