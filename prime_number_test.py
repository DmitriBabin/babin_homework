import time as t
import random as rd
import math

a_num = rd.randint(2,500)

start_time = t.time()
# Проверка делением
def prime(a_num):
    i = 2
    j = 0
    while i ** 2 <= a_num and j != 1:
        if a_num % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    return True

print('Проверка делением:', a_num, prime(a_num))
print(" %s секунд " % (t.time() - start_time))
start_time = t.time()
# используя теорему Вильсона
def vilson_prime(a_num):
    if (math.factorial(a_num - 1 ) + 1) % a_num != 0:
        return False
    return True

print('Проверка теоремой Вильсона:', a_num, vilson_prime(a_num))
print(" %s секунд " % (t.time() - start_time))

start_time = t.time()
# тест Миллреа-Рабина (вероятностный тест)
# тест параметризуется количеством раундов, которые рекомендуется
#брать порядка логарифма проверяемого числа по основанию 2
def to_binary(a_num):
    r_num = []
    while (a_num > 0):
        r_num.append(a_num % 2)
        a_num = a_num / 2
        return r_num

def m_r_test(a_num):
    for j in range(1, 100):
            a_num2 = rd.randint(1, a_num - 1)
            b_num = to_binary(a_num - 1)
            c_num = 1
            for i in range(len(b_num) - 1, -1, -1):
                x_num = c_num
                c_num = (c_num ** 2) % a_num
                if c_num == 1 and x_num != 1 and x_num != a_num - 1:
                    return False
                if b_num[i] == 1:
                    c_num = (c_num * a_num2) % a_num
                    if c_num != 1:
                        return False
                    return True

print('Проверка по тесту Миллера-Рабина:', a_num, m_r_test(a_num))
print(" %s секунд " % (t.time() - start_time))
