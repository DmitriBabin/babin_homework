import math
import itertools as it

class Factorial:
    class Factorialiter:
        def __init__(self):
            self.i = 1
            self.z = 1
        def __next__(self):
            self.z *= self.i
            self.i += 1
            return self.z

    def __iter__(self):
        return Factorial.Factorialiter()

for w in it.islice(Factorial(), 10):
    print(w)
