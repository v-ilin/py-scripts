import json


# with(open("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\instances_train2014.json", "r")) as cocoTrain:
#     trainData = json.load(cocoTrain)

with(open("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\instances_val2014.json", "r")) as cocoVal:
    valData = json.load(cocoVal)

resultValData = dict()
resultValData["images"] = []
resultValData["annotations"] = []
resultValData["categories"] = []

# for ann in trainData["annotations"]:
#     if ann["category_id"] != 1:

for ann in valData["annotations"]:
    if ann["category_id"] == 1:
        resultValData["annotations"].append(ann)
        existingResultImg = None
        for img in resultValData["images"]:
            if img["id"] == ann["image_id"]:
                existingResultImg = img
                break;

        if existingResultImg is None:
            for img in valData["images"]:
                if img["id"] == ann["image_id"]:
                    cocoImg = img
                    break;
            resultValData["images"].append(cocoImg)

for cat in valData["categories"]:
    if cat["name"] == "person":
        resultValData["categories"].append(cat)
        break;

# with(open("e:\\Dev\\datasets\\coco-persons\\instances_train2014.json", "w")) as personsTrain:
#     json.dump(trainData, personsTrain)

with(open("e:\\Dev\\datasets\\coco-persons\\instances_val2014.json", "w")) as personsTrain:
    json.dump(resultValData, personsTrain)