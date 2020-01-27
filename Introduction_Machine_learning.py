#[1]
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
#print("x:\n{}".format(x))
print(f"x: \n {x}")

#[2]
from scipy import sparse
#create a 2D NumPy array with a diagonal of ones, and zeroes everywhere else
eye = np.eye(4)
print(f"NumPy array \n{eye}")

#[3]
# converting Numpy array into SciPy sparse matrix in CSR format
#Only the nonZero entries are stored
sparse_matrix = sparse.csr_matrix(eye)
print(f"\nSciPy sparse CSR Matrix:\n{sparse_matrix}")


#[4]
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data,(row_indices,col_indices)))

print(f"COO representation:\n{eye_coo}")

#[5]
import inline
#inline : matplotlib
#%matplotlib inline
#'exec(%matplotlib inline)'
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
#generate sequence of numbers from -10 to 10 with 100 steps in between
x =np.linspace(-10,10,100)

# create second array using sine
y = np.sin(x)

# plot function makes a line  chart of one array against another
plt.plot(x,y,marker="x")
#plt.show()


#[6]
import pandas as pd
from IPython.display import display

#create simple dataset of people (Dictionary)
data = {'Name':["John","Anna","Peter","Linda"],
        'Location':["New York","Paris","Berlin","London"],
        'Age':[24,13,53,33]}

data_pandas = pd.DataFrame(data)
#IPyhton.display allows "pretty printing" of dataframes in jupyter notebook
display(data_pandas)

#[7]
#Select all rows  that have an age column greater than 30
display(data_pandas[data_pandas.Age>30])

#[8]
import sys
import pandas as pd
print(f"Python Version : {sys.version}")
print(f"Pandas Version : {pd.__version__}")

import matplotlib
print(f"matplotlib version : {matplotlib.__version__}")

import numpy as np
print("NumPy version : {} ".format(np.__version__))

import scipy as sp
print("SciPy Version : {} ".format(sp.__version__))

import IPython
print("IPython Version : {} ".format(IPython.__version__))

import sklearn
print("scikit-learn version : {} ".format(sklearn.__version__))