import json
# import cPickle as pickle

with open("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\person_keypoints_val2014.json", "r") as jsonFile:
    data = json.load(jsonFile)

# with open('e:\\Dev\\datasets\\results\\hardhats-without-filters\\detections.pkl', 'rb') as handle:
#     b = pickle.load(handle)

a = ""