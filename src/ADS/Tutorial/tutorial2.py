# Sort the array on Red (0), White(1) and Blue(2)
def dijkstra_search(array):
    n = len(array)
    r = -1
    o = 0
    b = n

    # i = 1
    # while o < i < b:
    # for o in range(0, n - 1):
    while o < n - 1:
        if array[o] == 0:
            array[o], array[r + 1] = array[r + 1], array[o]
            r += 1
            o += 1
        elif array[o] == 1:
            # array[i], array[o] = array[o], array[i]
            o += 1
        else:
            array[o], array[b - 1] = array[b - 1], array[o]
            b -= 1
            #o -= 1
    return array


if __name__ == '__main__':
    arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    arr2 = [2, 2, 2, 0, 0, 0, 1, 1, 1]
    # 1 1 1 0 0 0 2 2 2
    #
    #
    #
    print(dijkstra_search(arr))
    print(dijkstra_search(arr2))
