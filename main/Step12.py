import numpy as np

from lib import add
from lib.Variable import Variable

print("\n---Add---\n")

x0 = Variable(np.array(2))
x1 = Variable(np.array(3))
y = add(x0, x1)
print(y.data)
