import numpy as np


class Variable:
    def __init__(self, data: np.ndarray):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError("Datatype not supported : {}".format(type(data)))

        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)

            print('f.inputs ----> ', ' '.join(map(str, f.inputs)))
            print('gxs      ----> ', gxs)
            print('zipped results ',
                  ['x: ' + str(x).replace('\n', '').replace('\t', '') + ' / gx: ' + str(gx) for x, gx in
                   zip(f.inputs, gxs)])
            print('\n')

            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx

                if x.creator is not None:
                    funcs.append(x.creator)

    def __str__(self):
        data = np.array_str(self.data)

        grad = None
        if self.grad is not None:
            grad = np.array_str(self.grad) if isinstance(self.grad, np.ndarray) else str(self.grad)

        creator = self.creator
        return '\n\tVaraible - data: {}, grad: {}, creator: {}'.format(data, grad, creator)
