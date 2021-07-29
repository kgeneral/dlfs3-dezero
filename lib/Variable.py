import numpy as np


class Variable:
    def __init__(self, data: np.ndarray):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError("Datatype not supported : {}".format(type(data)))

        self.data = data
        self.grad = None
        self.creator = None
        self.generation = 0

    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = []
        seen_set = set()

        def add_func(f):
            if f not in seen_set:
                funcs.append(f)
                seen_set.add(f)
                funcs.sort(key=lambda x: x.generation)

        add_func(self.creator)

        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output().grad for output in f.outputs]
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
                    add_func(x.creator)

    def cleargrad(self):
        self.grad = None

    def __str__(self):
        data = np.array_str(self.data)

        grad = None
        if self.grad is not None:
            grad = np.array_str(self.grad) if isinstance(self.grad, np.ndarray) else str(self.grad)

        creator = self.creator
        generation = self.generation
        return '\n\tVaraible - data: {}, grad: {}, creator: {}, generation: {}'.format(data, grad, creator, generation)
