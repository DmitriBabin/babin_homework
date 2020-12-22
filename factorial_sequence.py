import math
import itertools as it

def make_inf_sequence():
    x_num = 0
    while True:
        yield x_num
        x_num = x_num + 1
class Factorial:
    class Factorialiter:
        def __init__(self):
            self.i = 0
            self.fact = make_inf_sequence()
        def __next__(self):
            for self.i in self.fact:
                a_num = math.factorial(self.i)
                self.i += 1
                return a_num

    def __iter__(self):
        return Factorial.Factorialiter()

for w in it.islice(Factorial(), 10):
    print(w)