import math

def gcd(a_number,b_number):
    if b_number == 0:
        return a_number
    else:
        return gcd(b_number, a_number % b_number)

def extended_gcd(a_number,b_number):
    if a_number == 0:
        return (0, 1)
    else:
        x_num , y_num = extended_gcd(b_number % a_number, a_number)
    return ( y_num - (b_number // a_number) * x_num, x_num)
print(__name__,"was imported")
