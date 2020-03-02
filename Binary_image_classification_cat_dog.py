# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:17:03 2020

@author: hp
"""

import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.image as mpimg
import matplotlib.pyplot as plt





# let us view some images
for i in range(10):
        
    plt.figure(figsize = (12, 5))
    sp = plt.subplot(2, 5, i+1)
   # sp.axis("off")
    img = mpimg.imread("C:/Users/hp/Desktop/Image Datasets/Cat Vs Dog/training_set/dogs/dog." + str(i+1) +".jpg")
    plt.imshow(img)
    
###############################################################################
    
import tensorflow as tf 


train_dir = "C:/Users/hp/Desktop/Image Datasets/Cat Vs Dog/training_set"

test_dir = "C:/Users/hp/Desktop/Image Datasets/Cat Vs Dog/test_set"


from tensorflow.keras.preprocessing.image import ImageDataGenerator

# All images rescaled by 1./255
train_datagen = ImageDataGenerator(rescale = 1.0 / 255.0)
test_datagen = ImageDataGenerator(rescale = 1.0 / 255.0)

# Flow training images in batch of 32 using train_datagen generator

train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size = 32,
                                                    class_mode = "binary",
                                                    target_size = (150, 150))


# Flow validation images in batch of 32 using test_datagen generator

validation_generator = test_datagen.flow_from_directory(test_dir,
                                                        batch_size = 32,
                                                        class_mode = "binary",
                                                        target_size = (150, 150))



train_generator

validation_generator

###############################################################################

# Formation of Convolutional Neural Network (CNN)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten


model = Sequential([
        # Note the imput shape is the desired size of the image 150 * 150 with 
        # 3 bytes color
        
        Conv2D(16, (3, 3), activation = "relu", input_shape = (150, 150, 3) ),
        MaxPooling2D(2, 2),
        Conv2D(32, (3,3), activation = "relu"),
        MaxPooling2D(2, 2),
        Conv2D(64, (3,3), activation = "relu"),
        MaxPooling2D(2, 2),
        
        # Flatten the results feed into the a DNN
        
        Flatten(),
        
        # 512 neuron hidden layer
        
        Dense(512, activation ="relu"),
        Dropout(0.1, seed = 2019),
        
        # 256 neuron hidden layer
        
        Dense(256, activation = "relu"),
        Dropout(0.1, seed = 2019),
        
        #Only one output neuron. it will contain a value from 0-1 
        #where 0 for cat  and 1 for dog
        
        Dense(1, activation = "sigmoid")
        
        
        ])
    
    
    
# following will show model summary

model.summary()    


from tensorflow.keras.optimizers import RMSprop

from tensorflow.keras.callbacks import EarlyStopping

monitor = EarlyStopping(monitor = 'val_loss', min_delta = 1e-3,
                        patience = 5, verbose = 1, mode = 'auto',
                        restore_best_weights = True)


model.compile(optimizer = RMSprop(lr = 0.001),
              loss = 'binary_crossentropy',
              metrics = ['accuracy']
              )


###############################################################################

# Fitting the Model

history = model.fit_generator(train_generator, 
                              validation_data = validation_generator,
                              steps_per_epoch = 100, epochs = 15,
                              validation_steps = 50,
                              verbose = 2, callbacks = [monitor]
                              )





###############################################################################
# Model testing on test data

test_generator = test_datagen.flow_from_directory(test_dir,
                                                  batch_size = 32,
                                                  class_mode = None,
                                                  target_size = (150, 150),
                                                  shuffle = False)


y_prob = model.predict_generator(test_generator, callbacks = [monitor])

pred_y = ["CAT" if probs<0.5 else "DOG" for probs in y_prob]
pred_y
type(pred_y)
len(pred_y)

len(test_generator)

print(test_generator)

y_prob

###############################################################################

validation_dir = "C:/Users/hp/Desktop/Image Datasets/Cat Vs Dog/validation_set"
validation_datagen = ImageDataGenerator(rescale = 1.0 / 255.0)

validation_generator1 = validation_datagen.flow_from_directory(validation_dir,
                                                              batch_size = 32,
                                                              class_mode = None,
                                                              target_size = (150,150)
                                                              )


y_prob = model.predict_generator(validation_generator, callbacks = [monitor])

pred_y = ["CAT" if probs<0.5 else "DOG" for probs in y_prob]
pred_y
type(pred_y)
len(pred_y)


