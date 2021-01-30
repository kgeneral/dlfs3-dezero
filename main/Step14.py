import numpy as np

from lib import add, square
from lib.Variable import Variable

print("\n---Add---\n")

x = Variable(np.array(3.0))
y = add(x, x)

print('y', y.data)

y.backward()
print('x.grad', x.grad)

