import os
from os import listdir
from os.path import isfile, join
import shutil

base_dir = "e:\\dev\\datasets\\ann_results\\ann_results_3 (belt)\\separated\\train"
val_dir = "e:\\dev\\datasets\\ann_results\\ann_results_3 (belt)\\separated\\val"

files = [f for f in listdir(base_dir) if isfile(join(base_dir, f))]

for i, filename in enumerate(files):
    name, extension = os.path.splitext(filename)

    if extension != ".jpg" or i % 10 != 0:
        continue

    shutil.move(os.path.join(base_dir, filename), os.path.join(val_dir, filename))

    annotation_filename = name + ".xml"
    shutil.move(os.path.join(base_dir, annotation_filename), os.path.join(val_dir, annotation_filename))
