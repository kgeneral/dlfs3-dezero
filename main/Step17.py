import numpy as np
from memory_profiler import profile

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


@profile
def test_memory_usage():
    for i in range(10):
        x = Variable(np.random.randn(10000000))
        y = square(square(square(x)))


test_memory_usage()

"""
$ python -m memory_profiler ./main/Step17.py

before weakref

Filename: ./main/Step17.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     35.5 MiB     35.5 MiB           1   @profile
    55                                         def test_memory_usage():
    56   3087.5 MiB      0.0 MiB          11       for i in range(10):
    57   2858.6 MiB    763.0 MiB          10           x = Variable(np.random.randn(10000000))
    58   3087.5 MiB   2288.9 MiB          10           y = square(square(square(x)))
    
after weakref

Filename: ./main/Step17.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     35.5 MiB     35.5 MiB           1   @profile
    55                                         def test_memory_usage():
    56    645.9 MiB      0.0 MiB          11       for i in range(10):
    57    645.9 MiB    152.6 MiB          10           x = Variable(np.random.randn(10000000))
    58    645.9 MiB    457.8 MiB          10           y = square(square(square(x)))

generate image of memory benchmarks

$ pip install matplotlib
$ mprof run ./main/Step17.py
$ mprof plot -o image.png --backend agg
"""