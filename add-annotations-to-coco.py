import json


def get_max_id(dict, dict_key):
    max = 0

    for img in dict[dict_key]:
        if img["id"] > max:
            max = img["id"]

    return max


with open("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\instances_train2014.json", "r") as cocoTrain:
    cocoTrainData = json.load(cocoTrain)

with open("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\instances_val2014.json", "r") as cocoVal:
    cocoValData = json.load(cocoVal)

with open("e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\instances_train2014.json", "r") as hardhatsTrain:
    hardhatsTrainData = json.load(hardhatsTrain)

with open("e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\instances_val2014.json", "r") as hardhatsVal:
    hardhatsValData = json.load(hardhatsVal)

for imageTrain in hardhatsTrainData["images"]:
    cocoTrainData["images"].append(imageTrain)

ann_max_id = get_max_id(cocoTrainData, "annotations")
for annTrain in hardhatsTrainData["annotations"]:
    ann_max_id += 1
    annTrain["id"] = ann_max_id
    cocoTrainData["annotations"].append(annTrain)

for categoryTrain in hardhatsTrainData["categories"]:
    cocoTrainData["categories"].append(categoryTrain)

for imageVal in hardhatsValData["images"]:
    cocoValData["images"].append(imageVal)

ann_max_id = get_max_id(cocoValData, "annotations")
for annVal in hardhatsValData["annotations"]:
    ann_max_id += 1
    annVal["id"] = ann_max_id
    cocoValData["annotations"].append(annVal)

for categoryVal in hardhatsValData["categories"]:
    cocoValData["categories"].append(categoryVal)

with open("e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\annotations_with_coco\\instances_train2014.json", "w") as cocoTrainWithHardhats:
    json.dump(cocoTrainData, cocoTrainWithHardhats)

with open("e:\\Dev\\datasets\\image-net\\n03492922\\images_with_filters\\annotations_with_coco\\instances_val2014.json", "w") as cocoValWithHardhats:
    json.dump(cocoValData, cocoValWithHardhats)