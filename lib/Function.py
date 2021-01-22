import numpy as np

import lib
from lib.Variable import Variable


class Function:
    def __call__(self, input: Variable) -> Variable:
        x = input.data
        y = self.forward(x)
        output = Variable(lib.as_array(y))
        output.set_creator(self)
        self.input = input  # memorize input variable
        self.output = output  # memorize output
        return output

    def forward(self, x: np.ndarray) -> np.ndarray:
        raise NotImplementedError()

    def backward(self, gy: np.ndarray) -> np.ndarray:
        raise NotImplementedError()
