import csv

hardhat_dict_key = '/m/01n5_8'

# annotations_hardhat = []
#
# with open('openimages/annotations_human_2017_11/2017_11/train/annotations-human.csv', encoding='utf8') as annotations:
#     annF = open('hardhat_ann.csv', 'w+', encoding='utf8')
#
#     annReader = csv.reader(annotations)
#
#     for annRow in annReader:
#         if annRow[2] == hardhat_dict_key:
#             annotations_hardhat.append(annRow[0])
#             annF.write(",".join(annRow) + '\n')
#
#     annF.close()
#
# with open('openimages/images_2017_11/2017_11/train/images.csv', encoding='utf8') as csvFile:
#     reader = csv.reader(csvFile)
#
#     f = open('hardhat_images.csv', 'w+', encoding='utf8')
#
#     for row in reader:
#         if row[0] in annotations_hardhat:
#             print(row)
#             f.write(",".join(row) + '\n')
#
#     f.close()

with open('openimages/annotations_human_bbox_2017_11/2017_11/train/annotations-human-bbox.csv', encoding='utf8') as bboxAnn:
    bboxAnnReader = csv.reader(bboxAnn)

    with open('bbox_coordinates.csv', 'w+', encoding='utf8') as bboxFile:
        for row in bboxAnnReader:
            if row[2] == hardhat_dict_key:
                print(row)
                bboxFile.write(",".join(row[:-1]))
                bboxFile.write(row[-1] + '\n')
