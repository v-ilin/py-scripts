import json
import os
import shutil
from os import listdir
from os.path import isfile, join

data = json.load(open('mapping.json'))

onlyfiles = [f for f in listdir("o:\Temp\hardhat") if isfile(join("o:\Temp\hardhat", f))]

basedir = r"e:\Dev\datasets\image-net\hardhat"
movdir = r"e:\Dev\datasets\image-net\images"

# Walk through all files in the directory that contains the files to copy
for root, dirs, files in os.walk(basedir):
    for filename in files:
        # I use absolute path, case you want to move several dirs.
        old_name = os.path.join( os.path.abspath(root), filename )

        # Separate base from extension
        base, extension = os.path.splitext(filename)

        occurances = 0
        for link in list(data.values()):
            if filename in link:
                occurances += 1

        if occurances > 1:
            print(occurances)

        for key, value in data.items():

            if filename in value:
                new_name = os.path.join(movdir, key + extension)
                break

        if new_name == "" or new_name == None:
            print("File not found: {}".format(filename))
            continue

        # If folder basedir/base does not exist... You don't want to create it?
        # if not os.path.exists(os.path.join(basedir, base)):
        #     print(os.path.join(basedir,base), "not found")
        #     continue    # Next filename
        if not os.path.exists(new_name):  # folder exists, file does not
            shutil.copy(old_name, new_name)