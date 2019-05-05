#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:44:38 2019

@author: vipul
"""

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json

#Initializing the cnn
classifier=Sequential()

#Convolution
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu'))

#Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

#Adding the second convolutional layer and pooling layer
classifier.add(Convolution2D(32,3,3,activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

#Flattening
classifier.add(Flatten())

#Full Connection
classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))

#Compiling the CNN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)

training_set=train_datagen.flow_from_directory('dataset/training_set',
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode='binary')

test_set=test_datagen.flow_from_directory('dataset/test_set',
                                           target_size=(64,64),
                                           batch_size=32,
                                           class_mode='binary')

classifier.fit_generator(training_set,
                         samples_per_epoch=500,
                         nb_epoch=25,
                         validation_data=test_set,
                         nb_val_samples=20)

'''
Save the trained model
'''

# serialize model to JSON
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("model.h5")


# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")




"""
Making new predictions from the trained model
"""

#img=plt.imread('dataset/test_set/dogs/dog.4046.jpg')
#plt.imshow(img)
test_image=image.load_img('n3.jpeg',target_size=(64,64))
print(test_image)
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=loaded_model.predict(test_image)
#training_set.class_indices
if result[0][0]==1:
    prediction='Normal'
else:
    prediction='Pneumonia'

print('The given picture is',prediction)    
