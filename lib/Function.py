import numpy as np

import lib
from lib.Variable import Variable


class Function:
    def __call__(self, *inputs: [Variable]) -> Variable:
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)  # *xs : unpack [1,2,...] like (1,2,...)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(lib.as_array(y)) for y in ys]

        self.generation = max([x.generation for x in inputs])
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs  # memorize input variable
        self.outputs = outputs  # memorize output
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, *xs) -> np.ndarray:
        raise NotImplementedError()

    def backward(self, *gys) -> np.ndarray:
        raise NotImplementedError()

    def __str__(self):
        return "{}({})".format(self.__class__.__name__,
                               ",".join([str(x.data) for x in self.inputs]) if self.inputs is not None else ""
                               )
