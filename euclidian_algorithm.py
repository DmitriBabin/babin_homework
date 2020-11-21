import random as rd
import math

a_number = rd.randint(1, 100)
b_number = rd.randint(1, 100)
print('gcd(',a_number,',',b_number,')')
print('Значение, полученное встроенным алгоритмом = ', math.gcd(a_number,b_number))
def gcd(a_number,b_number):
    if b_number == 0:
        return a_number
    else:
        return gcd(b_number, a_number % b_number)

print('Значение, полученное встроенным алгоритмом = ', gcd(a_number,b_number))
