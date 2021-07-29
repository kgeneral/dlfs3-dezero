import numpy as np

from lib import add, square, exp
from lib.Function import Function
from lib.Variable import Variable

print("\n---Garbage collection---\n")


class Ref():
    def __init__(self):
        self.nextRef = []


# 1 ref for each
a = Ref()
b = Ref()
c = Ref()

# b got 2 refs now
a.nextRef = b
# c got 2 refs now
b.nextRef = c

# a will be deleted
# b also will be deleted : ref from a object has gone
# c also will be deleted : ref from b object has gone
a = b = c = None

# be aware of circular reference
# gc need to work for release "circular referenced objects"
# gc is an "expensive behavior"

print("\n---weakref---\n")

import weakref
import numpy as np

a = np.array([1, 2, 3])
b = weakref.ref(a)

print(b)
print(b())

a = None
# even b has reference of a, a will be deleted
# because b is weakref
print(b)

print("\n---big data---\n")
for i in range(10):
    x = Variable(np.random.randn(10000))
    y = square(square(square(x)))
