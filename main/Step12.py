import numpy as np

from lib import square, exp
from lib.Add import Add

from lib.Variable import Variable

print("\n---Add---\n")

x0 = Variable(np.array(2))
x1 = Variable(np.array(3))
f = Add()
y = f(x0, x1)
print(y.data)
