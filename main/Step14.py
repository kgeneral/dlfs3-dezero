import numpy as np

from lib import add, square
from lib.Variable import Variable

print("\n---Add---\n")

x = Variable(np.array(3.0))
y = add(x, x)
y.backward()
print('x.grad', x.grad)

x.cleargrad()
y = add(add(x, x), x)
y.backward()
print('x.grad', x.grad)
