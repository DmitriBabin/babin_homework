from numpy.linalg import norm
from numpy import array
from numpy.linalg import solve as solve_out_of_the_box

ab = array([
    [1.5, 2.0, 1.5, 2.0, 5.0],
    [3.0, 2.0, 4.0, 1.0, 6.0],
    [1.0, 6.0, 0.0, 4  , 7.0],
    [2.0, 1.0, 4.0, 3  , 8.0]
], dtype=float)

def vector_gauss(ab):
    ab = ab.copy()
    d = len(ab)

    for x in range(d):
        ab[x] = ab[x] / ab[x,x]
        for i in range(x+1,d):
            ab[i] = ab[i] - ab[x]*ab[i,x]
    

    for x in range(2, d+1):
        for i in range(d-x, -1, -1):
            ab[i] = ab[i] - ab[d-x+1]*ab[i,d-x+1]


    x = ab[:, -1]
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

solution = vector_gauss(ab)
oob_solution = solve_out_of_the_box(a, b)

print(__name__,"was imported")
