import multiprocessing as mp
import time as t
import random as rd

s = 0
def circle_test(s):
    a_num = rd.uniform(0,1)
    b_num = rd.uniform(0,1)
    if a_num**2 + b_num**2 <= 1:
        s += 1
    return s

def mult_test(pool):
    s_func = pool.map(circle_test, [0] * 10000)
    return s_func

if __name__ == '__main__':
    pool = mp.Pool()
    t1 = t.time()
    a = mult_test(pool)
    b = 0
    for i in range(10000):
        b += a[i]
    #Используя метод Монте-Карло (pi/4 = вероятность попадания в окружность, а не в квадрат со стороной = 2 радиусам):
    num_pi = (b * 4) / 10000
    print("Количество точек из 10000, попавших в окружность =", b)
    print("Приближённое пи =", num_pi)
    print("Длительность:", t.time() - t1)
else:
    print(__name__)
