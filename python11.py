# two layer perceptron: linear classification
import numpy as np
import pandas as pd
# sigmoid function
# deriv = true
def nonlin(x, deriv=False):
    if(deriv == True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
# input dataset
X = np.array([[0,0,1],
              [1,1,1],
              [1,0,1],
              [0,1,1]])
# output dataset
y = np.array([[0,1,1,0]]).T

# seed random numbers to make calculation, the seed method is called when RandomState is initialized.
np.random.seed(0)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

print syn0

syn1 = np.random.random_sample((5,))

print syn1

syn2 = 5*np.random.random_sample((3,2)) - 5

print syn2
# iteration
for iter in xrange(10000):
# forward propagation
# I0 input layer
  I0 = X
# zhangliang, 1-D normal multiplication;  2-D matrix multiplication
  I1 = nonlin(np.dot(I0,syn0))
# loss
  I1_error = y - I1
# multiply how much we missed by the slope of the sigmoid at the values in I1
  I1_delta = I1_error * nonlin(I1, True)
# update weights
  syn0 += np.dot(I0.T, I1_delta)

print ("Output After Training")
print I1
print ("==============")
print syn0