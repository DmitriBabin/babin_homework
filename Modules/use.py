print()
from packages import modulegauss
import moduleeuclid

from numpy import array
import random as rd
#Будем использовать необходимые нам значения
ab_vect = array([
    [1.5, 2.0, 1.5, 2.0, 5.0],
    [3.0, 2.0, 4.0, 1.0, 6.0],
    [1.0, 6.0, 0.0, 4  , 7.0],
    [2.0, 1.0, 4.0, 3  , 8.0]
], dtype=float)

a_num = rd.randint(1, 100)
b_num = rd.randint(1, 100)

#Пустые строки для удобства различения программ
print()
print("Метод Гаусса")
print("Для", ab_vect)
print(modulegauss.vector_gauss(ab_vect))
print()
print("Алгоритм Евклида")
print("gcd(",a_num,",",b_num,") =",moduleeuclid.gcd(a_num,b_num))
print()
print("Расширенный алгоритм Евклида для тех же чисел")
print(a_num,'*',(moduleeuclid.extended_gcd(a_num,b_num))[0],'+',b_num,'*',(moduleeuclid.extended_gcd(a_num,b_num))[1], '=',moduleeuclid.gcd(a_num,b_num))
