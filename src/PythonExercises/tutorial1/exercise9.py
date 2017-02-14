import itertools


def div_by_1to20(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True


def smallest_div1to20():
    i = 20
    while True:
        if div_by_1to20(i):
            return i
        else:
            i += 20


print('Smallest number divisible by numbers 1 to 20 is: %d' % smallest_div1to20())      # 232792560
