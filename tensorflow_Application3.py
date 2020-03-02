# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:27:28 2020

@author: hp
"""

"""
Ploblem statement :
TensorFlow application which creates two nodes which are constant and perform multiplication operation
an run it with the session.
We use  TensorBoard to display the Neural Network

"""


import tensorflow as tf


#Build Computational graph
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)


output = node1 * node2 

# Run computational graph
sobj = tf.compat.v1.Session()

File_Writer = tf.compat.v1.summary.FileWriter("Demo_TensorFlow", sobj.graph)
print(sobj.run(output))

sobj.close() 
