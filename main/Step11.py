import numpy as np

from lib import square, exp
from lib.Add import Add

from lib.Variable import Variable

print("\n---Add---\n")

xs = [Variable(np.array(2)), Variable(np.array(3))]
f = Add()
ys = f(xs)
y = ys[0]
print(y.data)
