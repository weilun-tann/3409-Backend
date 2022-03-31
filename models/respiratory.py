#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv("patient_diagnosis.csv")
data


# Each audio file name is divided into 5 elements, separated with underscores (_).
# 
# 1. Patient number (101,102,...,226)
# 2. Recording index
# 3. Chest location 
#       a. Trachea (Tc)
#       b. Anterior left (Al)
#       c. Anterior right (Ar)
#       d. Posterior left (Pl)
#       e. Posterior right (Pr)
#       f. Lateral left (Ll)
#       g. Lateral right (Lr)
# 4. Acquisition mode 
#      a. sequential/single channel (sc), 
#      b. simultaneous/multichannel (mc)
# 5. Recording equipment 
#      a. AKG C417L Microphone (AKGC417L), 
#      b. 3M Littmann Classic II SE Stethoscope (LittC2SE), 
#      c. 3M Litmmann 3200 Electronic Stethoscope (Litt3200), 
#      d.  WelchAllyn Meditron Master Elite Electronic Stethoscope (Meditron)
# 
# 
# The abbreviations used in the diagnosis file are:
# - COPD: Chronic Obstructive Pulmonary Disease
# - LRTI: Lower Respiratory Tract Infection
# - URTI: Upper Respiratory Tract Infection

# In[3]:


data['Diagnosis'].value_counts()


# As the last 5 diseases are rare in this dataset, I will drop the patients with those conditions and focus only on the top 3 (COPD, Healthy and URTI).

# In[4]:


data = data[(data.Diagnosis != "Bronchiectasis") & (data.Diagnosis != "Pneumonia") & (data.Diagnosis != "Bronchiolitis")
 & (data.Diagnosis != "LRTI")  & (data.Diagnosis != "Asthma")]


# In[5]:


data.reset_index(drop=True, inplace=True)


# In[6]:


import os
all_files = os.listdir("audio_and_txt_files")
files = []
for i in all_files:
    if i[-3:] == "wav":
        files.append(i)
files = pd.DataFrame(files, columns = {"Name"})
files


# In[7]:


files['Diagnosis'] = ""

for i in range(len(files)):
    for j in range(len(data)):
        if files['Name'][i][:3] == str(data['ID'][j]):
            if data['Diagnosis'][j] == "Healthy":
                files['Diagnosis'][i] = 0
            elif data['Diagnosis'][j] == "URTI":
                files['Diagnosis'][i] = 1
            else:
                files['Diagnosis'][i] = 2


# In[8]:


files = files[(files.Diagnosis != "")]
files.reset_index(drop=True, inplace=True)
print(len(files))


# In[10]:


files['Diagnosis'].value_counts()


# In[11]:


copd = files[files['Diagnosis'] == 2]
files = files[files['Diagnosis'] != 2]


# In[12]:


copd = copd["Name"].tolist()


# In[13]:


import random
random.seed(0)
random.shuffle(copd)
copd = copd[:30]


# In[14]:


copd = pd.DataFrame(copd, columns = {"Name"})
copd["Diagnosis"] = 2


# In[15]:


#copd


# In[16]:


frame = [copd, files]
files = pd.concat(frame)
files


# In[17]:


files.reset_index(drop=True, inplace=True)


# In[18]:


files['Diagnosis'].value_counts()


# In[19]:


files.reset_index(drop=True, inplace=True)


# In[53]:


#testing on one data point
import librosa
l = []
for i in range(2):
    to_add = []
    file_name = "audio_and_txt_files\\" + files['Name'][i] 
    y, sr = librosa.load(file_name, mono=True) 
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    for n in mfcc:
            to_add.append(np.mean(n))
    print(to_add)
    l.append(to_add)
print(pd.DataFrame(l))


# In[20]:


import librosa

files["chroma"] = ""
files["spec_cent"] = ""
files["spec_bw"] = ""
files["rolloff"] = ""
files["zcr"] = ""
feature = []


for i in range(len(files)):
    file_name = "audio_and_txt_files\\" + files['Name'][i]
    y, sr = librosa.load(file_name, mono=True) 
    to_add = []
    
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    for n in mfcc:
        to_add.append(np.mean(n))
    files["chroma"][i] = np.mean(chroma_stft)
    files["spec_cent"][i] = np.mean(spec_cent)
    files["spec_bw"][i] = np.mean(spec_bw)
    files["rolloff"][i] = np.mean(rolloff)
    files["zcr"][i] = np.mean(zcr)
    feature.append(to_add)


# In[21]:


feature = pd.DataFrame(feature)
dataset = pd.concat([files, feature], axis=1)


# In[22]:


dataset.to_csv("dataset.csv", index = False)


# In[60]:


dataset = pd.read_csv("dataset.csv")


# In[61]:


from sklearn.preprocessing import LabelEncoder, StandardScaler 
from keras.utils import np_utils
y = dataset["Diagnosis"]
y=np_utils.to_categorical(lb.fit_transform(y))
scaler = StandardScaler()
X = dataset.drop(["Diagnosis", "Name"], axis = 1)
X = scaler.fit_transform(X)


# In[62]:


X.shape


# In[63]:


y.shape


# In[64]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)


# In[65]:


from tensorflow.keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten, Activation
from tensorflow.keras.optimizers import Adam
from sklearn import metrics
from keras import layers
from keras.backend import manual_variable_initialization 
manual_variable_initialization(True)


# In[66]:


model = Sequential()
model.add(layers.Dense(256, activation='relu', input_shape=(25,)))
model.add(Dense(256, input_shape=(40,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(y.shape[1]))
model.add(Activation('softmax'))
model.summary()


# In[67]:


model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')
model.fit(X_train, y_train, batch_size=10, epochs=10, verbose=1)


# In[68]:


test_accuracy=model.evaluate(X_test,y_test,verbose=0)
print(test_accuracy[1])


# In[69]:


print(np.argmax(model.predict(X_test), axis=1))


# In[70]:


print(np.argmax(y_test, axis=1))


# In[71]:


model_json = model.to_json()
with open("model_respiratory.json", "w") as json_file:
    json_file.write(model_json)


# In[72]:


model.save_weights("model_r_weights.h5")


# In[73]:


from keras.models import model_from_json
model = model_from_json(open('model_respiratory.json').read())
model.load_weights('model_r_weights.h5')
model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')


# In[79]:


import librosa

features = []


file_name = "audio_and_txt_files\\" + files["Name"][1]
print(file_name)
y, sr = librosa.load(file_name, mono=True) 
to_add = []

chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
for n in mfcc:
    to_add.append(np.mean(n))

features.append(np.mean(chroma_stft))
features.append(np.mean(spec_cent))
features.append(np.mean(spec_bw))
features.append(np.mean(rolloff))
features.append(np.mean(zcr))
features+=to_add

print(features)


# In[81]:


from sklearn.preprocessing import LabelEncoder, StandardScaler 
scaler = StandardScaler()
print(features)
f = np.array(features)
f = f.reshape(1,f.shape[0]) 
f = scaler.fit_transform(f)
print(model.predict(f))
print(np.argmax(model.predict(f), axis=1))


# In[82]:


files


# In[ ]:





# In[ ]:




