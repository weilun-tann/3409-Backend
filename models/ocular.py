#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import tensorflow as tf
from matplotlib.pyplot import imshow


# In[4]:


data = pd.read_excel("data.xlsx")
data


# Ocular Disease Intelligent Recognition (ODIR) is a structured ophthalmic database of 5,000 patients with age, color fundus photographs from left and right eyes and doctors' diagnostic keywords from doctors.
# 
# This dataset is meant to represent ‘‘real-life’’ set of patient information collected by Shanggong Medical Technology Co., Ltd. from different hospitals/medical centers in China. In these institutions, fundus images are captured by various cameras in the market, such as Canon, Zeiss and Kowa, resulting into varied image resolutions.
# Annotations were labeled by trained human readers with quality control management. They classify patient into eight labels including:
# 
# Normal (N),
# Diabetes (D),
# Glaucoma (G),
# Cataract (C),
# Age related Macular Degeneration (A),
# Hypertension (H),
# Pathological Myopia (M),
# Other diseases/abnormalities (O)

# In[5]:


data.columns


# In[6]:


left = data[['Left-Fundus', 'Left-Diagnostic Keywords', 'N', 'D', 'G','C', 'A', 'H', 'M', 'O']]
right = data[['Right-Fundus', 'Right-Diagnostic Keywords', 'N', 'D', 'G','C', 'A', 'H', 'M', 'O']]
left.columns=['Fundus', 'Diagnostic Keywords', 'N', 'D', 'G','C', 'A', 'H', 'M', 'O']
right.columns=['Fundus', 'Diagnostic Keywords', 'N', 'D', 'G','C', 'A', 'H', 'M', 'O']
frames = [right, left]
combined = pd.DataFrame(pd.concat(frames))
combined.reset_index(drop=True, inplace=True)


# In[7]:


combined['N'] = 0
combined['D'] = 0
combined['G'] = 0
combined['C'] = 0
combined['A'] = 0
combined['H'] = 0
combined['M'] = 0
combined['O'] = 0
combined["Diagnosis"] = 7
for i in range(len(combined)):
    if 'normal fundus' in combined['Diagnostic Keywords'][i]:
        combined['N'][i] = 1
        combined["Diagnosis"][i] = 0
    elif 'cataract' in combined['Diagnostic Keywords'][i]:
        combined['C'][i] = 1
        combined["Diagnosis"][i] = 1
    elif combined['Diagnostic Keywords'][i] == 'glaucoma':
        combined['G'][i] = 1
        combined["Diagnosis"][i] = 2
    elif "age-related" in combined['Diagnostic Keywords'][i]:
        combined['A'][i] = 1
        combined["Diagnosis"][i] = 3
    elif "myopia" in combined['Diagnostic Keywords'][i]:
        combined['M'][i] = 1
        combined["Diagnosis"][i] = 4
    elif "hypertensive" in combined['Diagnostic Keywords'][i]:
        combined['H'][i] = 1
        combined["Diagnosis"][i] = 5
    elif "proliferative retinopathy" in combined['Diagnostic Keywords'][i]:
        combined['D'][i] = 1
        combined["Diagnosis"][i] = 6
    else:
        combined['O'][i] = 1
        combined["Diagnosis"][i] = 7


# In[8]:


combined


# In[9]:


combined["Diagnosis"].value_counts()


# In[10]:


combined = combined[(combined.Diagnosis == 0) | (combined.Diagnosis == 1)]


# In[11]:


combined.reset_index(drop=True, inplace=True)


# In[12]:


combined


# In[13]:


combined.to_csv("combined.csv", index=False)


# In[2]:


combined = pd.read_csv("combined.csv")
combined


# In[15]:


from skimage import io
image = io.imread("All images\\" + combined["Fundus"][0])
print(image.shape)
print(image) 
io.imshow(image)


# In[3]:


combined.Diagnosis.value_counts()


# In[4]:


n = []
c = []

for i in range(len(combined)):
    if combined['Diagnosis'][i] == 0:
        n.append(combined['Fundus'][i])
    else:
        c.append(combined['Fundus'][i])


# In[5]:


import random
n = random.sample(n, 313)


# In[6]:


print(len(n))
print(len(c))


# In[7]:


from tensorflow.keras.preprocessing.image import load_img,img_to_array
import cv2
import os
import random
dataset_dir = "All images/"
image_size=200
dataset = []

def create_dataset(l, label):
    for i in l:
        image_path = os.path.join(dataset_dir,i)
        try:
            image = cv2.imread(image_path,cv2.IMREAD_COLOR)
            image = cv2.resize(image,(image_size,image_size))
            print("gotten image")
        except Exception as e:
            print(e)
        dataset.append([np.array(image),np.array(label)])
        print("appended!")
    return dataset
dataset = create_dataset(c,1)
dataset = create_dataset(n,0)


# In[9]:


random.shuffle(dataset)


# In[89]:


dataset[1][0][101]


# In[13]:


x = np.array([i[0] for i in dataset]).reshape(-1,image_size,image_size,3)
y = np.array([i[1] for i in dataset])


# In[71]:


x[0].shape


# In[15]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=10)


# In[9]:


from tensorflow.keras.applications import ResNet50
resnet = ResNet50(weights="imagenet", include_top = False, input_shape=(200,200,3))

for layer in resnet.layers:
    layer.trainable = False


# In[11]:


from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense

model = Sequential()
model.add(resnet)
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(1,activation="sigmoid"))

model.summary()


# In[19]:


model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])


# In[20]:


model.fit(x_train, y_train, batch_size=8, epochs=10,verbose=1)


# In[21]:


from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
y_pred = model.predict(x_test)
y_pred[y_pred <= 0.5] = 0
y_pred[y_pred > 0.5] = 1
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))


# In[39]:


model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)


# In[40]:


model.save_weights("model_weights.h5")


# In[2]:


from keras.models import model_from_json
model = model_from_json(open('model.json').read())
model.load_weights('model_weights.h5')


# In[10]:


import cv2
import numpy as np
import pandas as pd
combined = pd.read_csv("combined.csv")
image = cv2.imread("All images\\" + combined["Fundus"][5], cv2.IMREAD_COLOR)
image = cv2.resize(image,(200,200))
image = np.array(image).reshape(-1, 200,200,3)


# In[11]:


pred = model.predict(image)
if pred > 0.5:
    pred = 1
else:
    pred = 0
print(pred)


# In[7]:


combined[combined["Diagnosis"] == 1]


# In[ ]:




