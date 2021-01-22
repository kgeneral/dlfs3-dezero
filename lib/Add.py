import numpy as np

from lib.Function import Function


class Add(Function):
    def forward(self, xs: np.ndarray) -> np.ndarray:
        x0, x1 = xs
        y = x0 + x1
        return (y,)
