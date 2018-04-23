import json


def clear_coco(input_file_path, output_file_path):
    with(open(input_file_path, "r")) as inputFile:
        source_data = json.load(inputFile)

    resultData = dict()
    resultData["images"] = []
    resultData["annotations"] = []
    resultData["categories"] = []

    for ann in source_data["annotations"]:
        if ann["category_id"] == 1:
            resultData["annotations"].append(ann)

            existing_result_img = None
            for img in resultData["images"]:
                if img["id"] == ann["image_id"]:
                    existing_result_img = img
                    break;

            if existing_result_img is None:
                for img in source_data["images"]:
                    if img["id"] == ann["image_id"]:
                        cocoImg = img
                        break;
                resultData["images"].append(cocoImg)

    for cat in source_data["categories"]:
        if cat["name"] == "person":
            resultData["categories"].append(cat)
            break;

    with(open(output_file_path, "w")) as personsTrain:
        json.dump(resultData, personsTrain)


clear_coco("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\instances_val2014.json",
           "e:\\Dev\\datasets\\coco-persons\\instances_val2014.json")

clear_coco("e:\\Dev\\datasets\\coco\\annotations_trainval2014\\annotations\\instances_train2014.json",
           "e:\\Dev\\datasets\\coco-persons\\instances_train2014.json")