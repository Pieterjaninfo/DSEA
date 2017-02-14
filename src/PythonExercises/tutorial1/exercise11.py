import itertools


# Creates a n x m array filled with zeros
def create_grid(n, m):
    grid = []
    for i in range(0, n):
        grid.append([0] * m)
    return grid


print(create_grid(2, 3))
