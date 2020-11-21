import random as rd
import math

a = rd.randint(1, 100)
b = rd.randint(1, 100)
print('gcd(',a,',',b,')')
print('Значение, полученное встроенным алгоритмом = ', math.gcd(a,b))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print('Значение, полученное написанным алгоритмом = ', a+b)
