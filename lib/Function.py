import numpy as np

import lib
from lib.Variable import Variable


class Function:
    def __call__(self, *inputs: [Variable]) -> Variable:
        xs = [x.data for x in inputs]
        ys = self.forward(xs)
        outputs = [Variable(lib.as_array(y)) for y in ys]

        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs  # memorize input variable
        self.outputs = outputs  # memorize output
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, xs: np.ndarray) -> np.ndarray:
        raise NotImplementedError()

    def backward(self, gys: np.ndarray) -> np.ndarray:
        raise NotImplementedError()
