from numbers import Number

import numpy as np

from lib.Function import Function


class Exp(Function):
    def forward(self, x: Number) -> Number:
        return np.exp(x)
