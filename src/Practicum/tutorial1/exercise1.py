def get_multi3and5():
    return sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])


print('Sum of all multiples is: %d' % get_multi3and5())
