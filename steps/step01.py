class Variable:
    def __init__(self, data):
        self.data = data

    def __str__(self) -> str:
        return str(data)

import numpy as np
data = np.array(1.0)
x = Variable(data)
print(x)