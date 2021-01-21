from numbers import Number

from lib.Function import Function


class Square(Function):
    def forward(self, x: Number) -> Number:
        return x ** 2
