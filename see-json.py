import json
# import cPickle as pickle

with open("e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\annotations_with_coco\\instances_train2014.json", "r") as jsonFile:
    data = json.load(jsonFile)

# with open('e:\\Dev\\datasets\\results\\hardhats-without-filters\\detections.pkl', 'rb') as handle:
#     b = pickle.load(handle)

a = ""