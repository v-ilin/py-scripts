import os
import shutil
from os import listdir
from os.path import isfile, join

ann_folder_path = "e:\\Dev\\datasets\\image-net\\n03492922\\images"
base_img_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\Annotations_all"
mov_img_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\Annotations"

ann_files = [f for f in listdir(ann_folder_path) if isfile(join(ann_folder_path, f))]

for ann_filename in ann_files:
    ann_base, ann_extension = os.path.splitext(ann_filename)

    img_files = [f for f in listdir(base_img_dir) if isfile(join(base_img_dir, f))]

    for img_filename in img_files:
        img_base, img_extension = os.path.splitext(img_filename)
        if(img_base == ann_base):
            old_name = os.path.join(base_img_dir, img_filename)
            new_name = os.path.join(mov_img_dir, img_filename)
            shutil.copy(old_name, new_name)