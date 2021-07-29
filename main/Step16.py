import numpy as np

from lib import add, square, exp
from lib.Function import Function
from lib.Variable import Variable

print("\n---Generation---\n")

generations = [2, 0, 1, 4, 2]
funcs = []

for g in generations:
    f = Function()
    f.generation = g
    funcs.append(f)

print([f.generation for f in funcs])

print("\n---Generation : after sort---\n")

funcs.sort(key=lambda x: x.generation)
print([f.generation for f in funcs])

f = funcs.pop()
print(f.generation)