import numpy as np

from lib.Variable import Variable

# variable
data = np.array(1.0)
x = Variable(data)
print(x.data)

x.data = np.array(2.0)
print(x.data)

# ndim = number of dimensions
y = np.array(1)
print(y.ndim)

y = np.array([1, 2, 3])
print(y.ndim)

y = np.array([[1, 2, 3],
              [4, 5, 6]])
print(y.ndim)
