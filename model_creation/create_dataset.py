import cv2
import os
import pickle
from random import shuffle
import numpy as np
from tensorflow.keras.utils import to_categorical

data_path = '../train_data'
categories = os.listdir(data_path)
labels = [i for i in range(len(categories))]

label_dict = {}
cat_dict = {}

for i in range(len(categories)):
    label_dict[categories[i]] = labels[i]

for i in range(len(categories)):
    cat_dict[labels[i]] = categories[i]

print(label_dict)
print(cat_dict)
print(categories)
print(labels)

dict_file = open("data/ai_car.pkl", "wb")
pickle.dump(cat_dict, dict_file)
dict_file.close()

img_size = 50
dataset = []

for category in categories:
    folder_path = os.path.join(data_path, category)
    img_names = os.listdir(folder_path)

    for img_name in img_names:
        img_path = os.path.join(folder_path, img_name)
        img = cv2.imread(img_path)
        #cv2.imshow('LIVE',img)
        #cv2.waitKey(100)
        try:
            # Converting the image into gray scale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # resizing the gray scale into 50x50, since we need a fixed common size for all the images in the dataset
            resized = cv2.resize(gray, (img_size, img_size))

            # appending the image and the label(categorized) into the list (dataset)
            dataset.append([resized, label_dict[category]])
        except Exception as e:
            print(e)
            #if any exception raised, the exception will be printed here. And pass to the next image

len(dataset)

shuffle(dataset)

data = []
target = []

for feature, label in dataset:
    data.append(feature)
    target.append(label)

data = np.array(data) / 255.0
data = np.reshape(data, (data.shape[0], img_size, img_size, 1))
target = np.array(target)

new_target = to_categorical(target)

np.save('data/data', data)
np.save('data/target', new_target)
