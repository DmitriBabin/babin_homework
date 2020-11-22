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

def extended_gcd(a_number,b_number):
    if a_number == 0:
        return (0, 1)
    else:
        x_num , y_num = extended_gcd(b_number % a_number, a_number)
    return ( y_num - (b_number // a_number) * x_num, x_num)
print(a_number, '*', extended_gcd(a_number,b_number)[0], '+', b_number,
      '*', extended_gcd(a_number,b_number)[1], '=' , gcd(a_number,b_number))
