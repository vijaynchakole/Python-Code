# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:32:55 2020

@author: hp
"""
import numpy as np
import tensorflow.compat.v1 as tf


# Define the variables
X_1 = tf.placeholder(tf.float32, name = "X_1")
X_2  = tf.placeholder(tf.float32, name = "X_2")


# Define the computation

multiply = tf.multiply(X_1, X_2, name = "multiply")

# Execute the operation
with tf.Session() as sess:
    result = sess.run(multiply, feed_dict = {X_1 : [1,2,3], X_2:[4,5,6]})
    print(result)

################################################################################
    
# options to load data in tensorflow

# create tensorflow pipeline

# create the data 

#  let's use numpy library to generate two random values. 

x_input = np.random.sample((1,2)) #sample(rows,columns)
x_input    


# create the placeholder
#using a placeholder
"""
 we create a placeholder with the name X. We need to specify the shape of the tensor explicitly. 
 In case, we will load an array with only two values. We can write the shape as shape=[1,2] 
 
"""

x = tf.placeholder(tf.float32, shape=[1,2], name = "X")

# Define dataset method

dataset = tf.data.Dataset.from_tensor_slices(x)

# Create the pipeline

"""
In step four, we need to initialize the pipeline where the data will flow.
 We need to create an iterator with make_initializable_iterator. We name it iterator. 
 Then we need to call this iterator to feed the next batch of data, get_next.
 We name this step get_next.
 Note that in our example, there is only one batch of data with only two values. 
"""
iterator = dataset.make_initializable_iterator()
get_next =iterator.get_next()


# execute the operation

with tf.Session() as sess:
    # feed the placeholder with data
    sess.run(iterator.initializer, feed_dict = {x:x_input})
    print(sess.run(get_next))