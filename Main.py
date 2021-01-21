import numpy as np

from lib.Square import Square
from lib.Variable import Variable

# variable
print("\n---variable---\n")

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

# function
print("\n---function---\n")

x = Variable(np.array(10))
f = Square()
y = f(x)

print(type(y))
print(y.data)
