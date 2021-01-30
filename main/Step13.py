import numpy as np

from lib import add, square
from lib.Variable import Variable

print("\n---Square---\n")

x = Variable(np.array(2.0))
y = Variable(np.array(3.0))

z = add(square(x), square(y))
z.backward()
print(z.data)
print(x.grad)
print(y.grad)
