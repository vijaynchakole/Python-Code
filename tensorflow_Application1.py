# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:04:05 2020

@author: hp
"""


"""
ploblem statement:
    
Tensorflow application which creates two nodes which are constant and  run  it with the Session.

"""

"""

The thing is

The tensorflow core r2.0 have enabled eager execution by default so doesn't need to write tf.compat.v1.Session() and use .run() function
If we want to use tf.compat.v1.Session() then we need to do thi
tf.compat.v1.disable_eager_execution() in the starting of algorithm. Now we can use tf.compat.v1.Session() and .run() function.

Tensorflow core r2.0 have enabled eager execution by default. so, without changing it

"""
import tensorflow as tf

tf.compat.v1.disable_eager_execution()


"""
Eager execution is a flexible machine learning platform for research and experimentation, 
providing: An intuitive interface—Structure your code naturally and use Python data structures.
Quickly iterate on small models and small data. 
Easier debugging—Call ops directly to inspect running models and test changes.
"""
#build computational graph
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)

print(node1, node2)

#Run computational graph
sobj = tf.compat.v1.Session()


print(sobj.run([node1, node2]))

sobj.close()

########## OR ##############################


# Launch the graph in a session.
 with tf.compat.v1.Session() as ses:

     # Build a graph.
     a = tf.constant(5.0)
     b = tf.constant(6.0)
     c = a * b

     # Evaluate the tensor `c`.
     print(ses.run(c))