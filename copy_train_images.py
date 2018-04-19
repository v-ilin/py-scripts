import json
import shutil
import os
from os.path import isfile, join

base_img_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\images\\"
mov_img_dir = "e:\\Dev\\datasets\\image-net\\n03492922\\val_images\\"

with open("e:\\Dev\\datasets\\image-net\\n03492922\\instances_val2014.json", "r") as train:
    trainData = json.load(train)

for image in trainData["images"]:
    filename = image["file_name"] + ".jpg"
    old_name = base_img_dir + filename
    new_name = mov_img_dir + filename

    shutil.copy(old_name, new_name)