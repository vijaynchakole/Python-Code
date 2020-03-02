# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:18:02 2020

@author: hp
"""

"""
tensorflow  application which calculate Loss

"""

import tensorflow.compat.v1 as tf

#Model paramenter

w = tf.compat.v1.Variable([0.3], tf.float32)
b = tf.compat.v1.Variable([-0.3], tf.float32)

# w = -1, b = 1

# input and output
x = tf.compat.v1.placeholder(tf.float32)

linear_model = w*x + b

y = tf.compat.v1.placeholder(tf.float32)

# Loss function

squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)

init = tf.global_variables_initializer()

# Run computational graph
sobj = tf.compat.v1.Session()

sobj.run(init)

print(sobj.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

sobj.close()
