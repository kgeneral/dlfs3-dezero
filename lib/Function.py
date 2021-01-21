from numbers import Number

from lib.Variable import Variable


class Function:
    def __call__(self, input: Variable) -> Variable:
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x: Number) -> Number:
        raise NotImplementedError()
