# Exercise 1 - worst case 8 comparisons
def get_middle(a, b, c):
    if b <= a <= c or c <= a <= b:
        return a
    elif a <= b <= c or c <= b <= a:
        return b
    else:
        return c

# worst case: 3, average case:
def get_middle2(a, b, c):
    mid = -1
    if a < b:           # 4 cases
        if b < c:       #
            mid = b
        elif a < c:
            mid = c
        else:
            mid =  a
    else: # a >= b      # 2 cases
        if a < c:
             mid = a
        elif c < b:
            mid =  b
        else:
            mid = c
    return mid


# Exercise 2 - worst case (n-1) comparisons
# better: two lists big,small, and get min/max from those
def get_minmax(array):
    min_value = array[0]
    max_value = array[0]

    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
        if array[i] > max_value:
            max_value = array[i]
    return (min_value, max_value)




print(get_middle(1, 0, 2))
print(get_middle2(1, 0, 2))
print(get_minmax([1,6,3,7,9,5324,12,-142,562,-1,-420]))



