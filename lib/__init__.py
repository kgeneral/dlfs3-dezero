import numpy as np

from lib.Add import Add
from lib.Exp import Exp
from lib.Square import Square


def square(x):
    return Square()(x)


def exp(x):
    return Exp()(x)


def add(x0, x1):
    return Add()(x0, x1)


def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x
