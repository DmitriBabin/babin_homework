import numbers
import itertools


class PolynomialDomainError(ValueError):
    pass


class Polynomial:

    def __init__(self, arg=0):
        if isinstance(arg, numbers.Number):
            self.coefficients = [arg]
        elif isinstance(arg, list):
            self.coefficients = arg.copy()
        elif isinstance(arg, Polynomial):
            self.coefficients = arg.coefficients.copy()
        else:
            raise PolynomialDomainError("You are trying to create polynomial from " + repr(arg))

        self.cleanup(self.coefficients)

    @staticmethod
    def cleanup(coefficients):
        """
        Многочлены определены в поле остатков по модулю 73 и x^4 = -1
        """
        for i in range(0,len(coefficients)):
            coefficients[i] = coefficients[i] % 73
        if len(coefficients) != 0:
            for i in range(4, len(coefficients)):
                a_num = i % 4
                coefficients[a_num] += coefficients[i]* ((-1) ** (i//4))

            while len(coefficients) - 4:
                del coefficients[-1]

    def __str__(self):
        return (" + ".join([
            str(c_num) + ("*x^" + str(i) if i > 0 else "")
            for c_num, i in reversed(list(zip(self.coefficients, itertools.count())))
        ])) if len(self.coefficients) else '0'


    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            other = Polynomial(other)

        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        else:
            raise PolynomialDomainError("Can't say if Polynomial is equal to " + str(type(other)))


    def __lshift__(self, deg):
        return Polynomial(([0] * deg) + self.coefficients)

    def __add__(self, other):
        if isinstance(other, numbers.Integral):
            other = Polynomial(other)

        sc_num = self.coefficients.copy()
        oc_num = other.coefficients.copy()

        sc_num += [0] * (len(oc_num)-len(sc_num))
        oc_num += [0] * (len(sc_num)-len(oc_num))

        return Polynomial([
            sce_num + oce_num for sce_num, oce_num in zip(sc_num, oc_num)
        ])


    def __radd__(self, other):
        return self.__add__(other)


    def __neg__(self):
        return Polynomial([-c_num for c_num in self.coefficients])


    def __sub__(self, other):
        if isinstance(other, numbers.Integral):
            other = Polynomial(other)

        return self.__add__(other.__neg__())


    def __rsub__(self, other):
        return self.__neg__().__add__(other)


    def __mul__(self, other):
        if isinstance(other, numbers.Integral):
            other = Polynomial(other)

        c_num = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for sc_num, sci_num in zip(self.coefficients, itertools.count()):
            for oc_num, oci_num in zip(other.coefficients, itertools.count()):
                c_num[sci_num + oci_num] += sc_num * oc_num

        return Polynomial(c_num)

    def __rmul__(self, other):
        return self.__mul__(other)


    def __divmod__(self, other):
        if isinstance(other, numbers.Integral):
            other = Polynomial(other)

        sc_num = Polynomial(self)
        oc_num = other
        d_num = []

        while len(sc_num.coefficients) >= len(oc_num.coefficients) > 0:
            c_num = sc_num.coefficients[-1] / oc_num.coefficients[-1]
            sc_num -= c_num * (oc_num << (len(sc_num.coefficients) - len(oc_num.coefficients)))
            d_num.append(c_num)

        return Polynomial(list(reversed(d_num))), sc_num


    def __floordiv__(self, other):
        return divmod(self, other)[0]

    def __mod__(self, other):
        return divmod(self, other)[1]


    def __rfloordiv__(self, other):
        return divmod(other, self)[0]

    def __rmod__(self, other):
        return divmod(other, self)[1]

    def __rdivmod__(self, other):
        return Polynomial(other).__divmod__(self)

    def __complex__(self):
        if not len(self.coefficients):
            return 0j
        elif len(self.coefficients) == 1:
            return complex(self.coefficients[0])
        else:
            raise PolynomialDomainError("Can't consider higher degree polynomial as a complex")


    def __float__(self):
        if not len(self.coefficients):
            return 0.0
        elif len(self.coefficients) == 1:
            return complex(self.coefficients[0])
        else:
            raise PolynomialDomainError("Can't consider higher degree polynomial as a float")


    def __int__(self) -> int:
        if not len(self.coefficients):
            return 0
        elif len(self.coefficients) == 1:
            return int(self.coefficients[0])
        else:
            raise PolynomialDomainError("Can't consider higher degree polynomial as an integer")

        return int(self.coefficients[0])


p1 = Polynomial([1,0,3,2,2,2,2,73])
p2 = Polynomial([72,0,3,2,2,3])
p3 = Polynomial([])
B1 = 3
print("p1:", p1, " ","p2:", p2, " " ,"p3",p3)
print("p1 + p2:", p1 + p2, " ", "p1 + p3:",p1 + p3)
print(p1 == p2)
print(p1 * p2)
print(complex(B1))
