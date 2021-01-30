import numpy as np

from lib.Function import Function


class Add(Function):
    def forward(self, x0, x1) -> np.ndarray:
        y = x0 + x1
        return y

    def backward(self, gy) -> np.ndarray:
        return gy, gy

