from src.Practicum.tutorial2.perm import *


def composition(p, q):
    return [q[i] for i in p]




def inverse(arrays):
    grid = []
    for array in arrays:
        new_array = array[1:]
        new_array.append(array[0])
        grid.append(new_array)
    return grid

if __name__ == '__main__':

    # p = [1, 2, 3, 0, 5, 6, 4, 8, 7]
    #
    # print()
    #
    # print('Composition [0,1,3,2] o [1,2,3,0] = %s' % str(composition([0,1,3,2], [1,2,3,0])))

    A = [0,1,2,3]
    Q = [2,1,0,3]
    Q2 = [[1,0,2],[3]]

    com = composition(A, Q)
    inv = inverse(Q2)

    print(com)
    print(inv)
    print(composition(com, Q2))



    # print(inverse([ [2], [0, 1], [3] ]))
    # print('===============================')
    # permutation_from_cycles(10,[])
    #

    # q =
    # r = 0
    # print(composition(q, r))
