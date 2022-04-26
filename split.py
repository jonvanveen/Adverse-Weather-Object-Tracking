"""
This script splits the bdd100k train and val data into time of day

After unzipping the bd100k files, the file hiearchy should be
--bd100k
   --images
      --train
         --*.jpg
      --val
         --*.jpg
   --labels
   --split.py

after running python3 split.py the file, the file hiearchy will be
--bd100k
   --images
      --train
        --daylight
          --*.jpg
        --night
          --*.jpg
        --duskdawn
          *.jpg
      --val
        --daylight
          --*.jpg
        --night
          --*.jpg
        --duskdawn
          *.jpg
   --labels
   --split.py
"""

import json 
import os
import shutil



train_json = "labels/bdd100k_labels_images_train.json"
val_json = "labels/bdd100k_labels_images_val.json"

# create directory for custom split

img_dir = "images/custom_100k/"

os.mkdir(img_dir)
#os.mkdir("custom_100k/test")
os.mkdir(img_dir + "train")
os.mkdir(img_dir + "val")

# create directory for time of day
os.mkdir(img_dir + "train/daytime")
os.mkdir(img_dir + "train/night")
os.mkdir(img_dir + "train/duskdawn")
os.mkdir(img_dir + "val/daytime")
os.mkdir(img_dir + "val/night")
os.mkdir(img_dir + "val/duskdawn")


day_list=[]
night_list=[]
duskdawn_list=[]

with open(train_json, "r") as f:
    data = json.load(f)

    for img in data:
        timeofday = img["attributes"]["timeofday"]
        filename = img["name"]

        if timeofday == "dawn/dusk":
            duskdawn_list.append(filename)
        if timeofday == "daytime":
            day_list.append(filename)
        if timeofday == "night":
            night_list.append(filename)
print("finished sorting")
for filename in day_list:
    shutil.copy("images/100k/train/" + filename, img_dir + "train/daytime")
print("finished saving train daytime")

for filename in night_list:
    shutil.copy("images/100k/train/" + filename, img_dir + "train/night")
print("finished saving train night")

for filename in duskdawn_list:
    shutil.copy("images/100k/train/" + filename, img_dir + "train/duskdawn")
print("finished saving train duskdawn")

day_list = []
night_list = []
duskdawn_list =[]

with open(val_json, "r") as f:
    data = json.load(f)

    for img in data:
        timeofday = img["attributes"]["timeofday"]
        filename = img["name"]

        if timeofday == "dawn/dusk":
            duskdawn_list.append(filename)
        if timeofday == "daytime":
            day_list.append(filename)
        if timeofday == "night":
            night_list.append(filename)

print("finished sorting")
for filename in day_list:
    shutil.copy("images/100k/val/" + filename, img_dir + "val/daytime")
print("finished saving val daytime")

for filename in night_list:
    shutil.copy("images/100k/val/" + filename, img_dir + "val/night")
print("finished saving val night")

for filename in duskdawn_list:
    shutil.copy("images/100k/val/" + filename, img_dir + "val/duskdawn")
print("finished saving val duskdawn")


