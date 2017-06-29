import numpy as np
# dot
a = np.eye(2)
print (a)
b = np.ones((2,2))*3
print (b)
print (a.dot(b))

print (np.dot(3,4))
c = [[1,0],[0,1]]
d = [[4,1],[2,2]]
print (np.dot(d, c))

# broadcast
e = np.array([0.0, 10.0, 20.0, 30.0, 40.0])
f = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
print(e[:, np.newaxis] + f)
