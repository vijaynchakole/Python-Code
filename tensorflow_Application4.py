# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:46:30 2020

@author: hp
"""

"""
TensorFlow application which creates two nodes which are placeholder and performs addition operation
and run it with the Session
"""

import tensorflow as tf

#Build computational graph
node1 = tf.compat.v1.placeholder(tf.float32)
node2 = tf.compat.v1.placeholder(tf.float32)
output = tf.compat.v1.placeholder(tf.float32)


output = node1 + node2

#Run computational graph
sobj = tf.compat.v1.Session()

print(sobj.run(output, {node1:[1.0,3.0], node2 : [4.0,5.0]}))

sobj.close()
