import random as rd
import math

a = rd.randint(1, 100)
b = rd.randint(1, 100)
print('gcd(',a,',',b,')')
print('Значение, полученное встроенным алгоритмом = ', math.gcd(a,b))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print('Значение, полученное встроенным алгоритмом = ', gcd(a,b))
