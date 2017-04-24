#three layer nn: tackle non-linear problems
import numpy as np
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
y = np.array([[0],
    [1],
    [1],
    [0]
])
np.random.seed(1)
# randomly initialize the weights with mean 0
syn0 = 2*np.random.random((3,5)) - 1
syn1 = 2*np.random.random((5,1)) - 1
for j in xrange(100000):
# feed forward through layers 0,1,and 2
 I0 = X
 I1 = nonlin(np.dot(I0,syn0))
 I2 = nonlin(np.dot(I1,syn1))
# I2 loss
 I2_error = y - I2
 if(j % 10000) == 0:
     print("Error:"+str(np.mean(np.abs(I2_error))))
 I2_delta = I2_error * nonlin(I2, deriv=True)
# I1 loss
 I1_error = I2_delta.dot(syn1.T)
 I1_delta = I1_error * nonlin(I1, deriv=True)
 syn1 += I1.T.dot(I2_delta)
 syn0 += I0.T.dot(I1_delta)

print("=====syn1======")
#print syn1
print("=====syn0======")
#print syn0
print("=====I2========")
print I2
print("=====I1========")
#print I1
