from lib.Variable import Variable


class Function:
    def __call__(self, input: Variable) -> Variable:
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output
