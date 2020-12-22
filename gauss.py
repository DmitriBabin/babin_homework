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

    for i in range(d+1):
        ab[0] = ab[0] / ab[0,0]

    for i in range(1,d):
        ab[i] = ab[i] - ab[0]*ab[i,0]

    for i in range(d+1):
        ab[1] = ab[1] / ab[1,1]

    for i in range(2,d):
        ab[i] = ab[i] - ab[1]*ab[i,1]

    for i in range(d+1):
        ab[2] = ab[2] / ab[2,2]

    for i in range(3,d):
        ab[i] = ab[i] - ab[2]*ab[3,2]

    for i in range(d+1):
        ab[3] = ab[3] / ab[3,3]


    for i in range(d-2, -1, -1):
        ab[i] = ab[i] - ab[d-1]*ab[i,d-1]

    for i in range(d-3, -1, -1):
        ab[i] = ab[i] - ab[d-2]*ab[i,d-2]


    for i in range(d-4, -1, -1):
        ab[i] = ab[i] - ab[d-3]*ab[i,d-3]


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

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
