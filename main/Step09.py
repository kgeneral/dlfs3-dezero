import numpy as np

from lib import square, exp
from lib.Variable import Variable

print("\n---square, exp as method---\n")

x = Variable(np.array(0.5))
y = square(exp(square(x)))
y.backward()
print(x.grad)

# x = Variable(1.0) # TypeError: Datatype not supported : <class 'float'>


