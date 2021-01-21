import numpy as np

from lib.Function import Function


class Square(Function):
    def forward(self, x: np.ndarray) -> np.ndarray:
        return x ** 2
