import numpy as np

from lib import add, square, exp
from lib.Variable import Variable

print("\n---Add---\n")

x = Variable(np.array(3.0))
a = square(x)
b = square(a)
c = square(a)
d = add(b, c)
y = square(d)

y.backward()
print('x.grad', x.grad)
