import numpy as np

from lib.Variable import Variable


class Function:
    def __call__(self, input: Variable) -> Variable:
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x: np.ndarray) -> np.ndarray:
        raise NotImplementedError()
