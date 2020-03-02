# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:20:17 2020

@author: hp
"""

import tensorflow as tf
from tensorflow import keras
keras.__version__
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import numpy as np

# Model building in Neural Network Using tensorflow keras

data = np.random.random((1000, 100))
labels = np.random.randint(2, size = (1000, 1))


model = Sequential()
model.add(Dense(32, activation = "relu", input_dim = 100))
model.add(Dense(1, activation = "sigmoid"))
model.compile(optimizer = "rmsprop", 
              loss = "binary_crossentropy",
              metrics = ["accuracy"])
model.fit(data, labels, epochs = 10, batch_size = 32)
predictions = model.predict(data)
predictions

###############################################################################

# Keras Data Sets

from tensorflow.keras.datasets import boston_housing, mnist, 
                                        fashion_mnist, cifar10, imdb
                                        
                                        
(X_train, y_train), (X_test, y_test) = mnist.load_data()

(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words = 20000)

n_classes = 20

###############################################################################

# Other

from urllib.request import urlopen
data = np.loadtxt(urlopen("required_dataset_link"))

###############################################################################

# Preprocessing
# Sequence Padding

from tensorflow.keras.preprocessing import sequence

x_train4 =sequence.pad_sequences(x_train4, maxlen = 80)
x_test4 = sequence.pad_sequences(x_test4, maxlen = 80)

# One-Hot Encoding
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

###############################################################################

# Model Architecture

from tensorflow import keras

from tensorflow.keras.models import Sequential

model = Sequential()

model2 = Sequential()

model3 = Sequential()

###############################################################################

# MultiLayer Perceptrons (MLP)

# Binary Classification

from tensorflow.keras.layers import Dense
model.add(Dense(12, input_dim = 8, kernel_initializer = 'uniform',
                activation = 'relu'))

model.add(Dense(8, kernel_initializer = "uniform",
                activation = "relu"))

model.add(Dense(1, kernel_initializer = 'uniform', activation = 'sigmoid'))



# MultiClass Classification

from tensorflow.keras.layers import Dropout

#first layer
model.add(Dense(512, activation = 'relu', input_shape = (784,)))
model.add(Dropout(0.2))

#Second layer
model.add(Dense(512, activation = 'relu'))
model.add(Dropout(0.2))

#output
model.add(Dense(10, activation = 'softmax'))


# Regression
# input_dim = number of features in our dataset that number of columns

model.add(Dense(64, activation = 'relu', input_dim = X_train.shape[1]))
model.add(Dense(1))



###############################################################################

# Convolutional Neural Networks (CNN)


from tensorflow.keras.layers import Activation, Conv2D, MaxPooling2D, Flatten

# first layer
model2.add(Conv2D(32, (3,3), padding = 'same', input_shape = X_train.shape[1:])) 
model2.add(Activation('relu'))
model2.add(Conv2D(32, (3,3)))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size = (2,2)))
model2.add(Dropout(0.25))

# Second layer
model2.add(Conv2D(64, (3,3), padding = 'same'))
model2.add(Activation('relu'))
model2.add(Conv2D(64, (3,3)))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size=(2,2)))
model2.add(Dropout(0.25))


#output
model2.add(Flatten())
model2.add(Dense(512))
model2.add(Activation('relu'))
model2.add(Dropout(0.50))
model2.add(Dense(n_classes))
model2.add(Activation('softmax'))


###############################################################################

# Recurrent Neural Network (RNN)
from tensorflow.keras.layers import Embedding, LSTM

model3.add(Embedding(20000, 128))
model3.add(LSTM(128, dropout = 0.2, recurrent_dropout = 0.2))
model3.add(Dense(1, activation = 'sigmoid'))

###############################################################################

# Inspect Model

# model output shape
model.output_shape

# model summary representation
model.summary()

# Model configuration
model.get_config()

# list all weights tensors in the model
model.get_weights()

###############################################################################

# Compile Model

# MLP : Binary Classification

model.compile(optimizer = 'adam', 
              loss = 'binary_crossentropy',
              metrics = ['accuracy'])


# MLP : Multi-Class Classification

model.compile(optimizer = 'rmsprop',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])


# MLP : Regression

model.compile(optimizer = 'rmsprop',
              loss = 'mse',
              metrics = ['mae'])


# Recurrent Neural Network

model3.compile(loss = 'binary_crossentropy',
               optimizer = 'adam',
               metrics = ['accuracy'])

# Convolutional Neural Network

model2.compile(optimizer = 'SGD',
               loss = 'categorical_crossentropy',
               metrics = ['accuracy'])


###############################################################################

# Model Training

model.fit(X_train, y_train, batch_size = 32,
           epochs = 15, verbose = 1, 
           validation_data = (X_test, y_test))

###############################################################################

# Evaluate Your  Model's Performance
score = model.evaluate(X_test, y_test, batch_size = 32)


###############################################################################
# Prediction
model3.predict(X_test, y_test, batch_size = 32)
model3.predict_classes(X_test, batch_size = 32)

###############################################################################

# Save / Reload Models

from tensorflow.keras.models import load_model
model3.save('model3_file.h5')
my_model  = load_model('model3_file.h5')


###############################################################################

# Model Fine-tuning

# Optimization Parameters

from tensorflow.keras.optimizers import RMSprop

opt = RMSprop(lr = 0.0001, decay = 1e-6)

model2.compile(loss = 'categorical_crossentropy',
               optimizer = opt,
               metrics = ['accuracy'])


###############################################################################

# Early Stopping

from tensorflow.keras.callbacks import EarlyStopping

early_stopping_monitor = EarlyStopping(patience = 5)

model3.fit(X_train, y_train, 
           batch_size = 32, epochs = 15, 
           validation_data = (X_test, y_test), 
           callbacks = [early_stopping_monitor])

