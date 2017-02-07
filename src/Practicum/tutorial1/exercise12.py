from random import randint


# n > 3, n is odd, k determines accuracy of test
def is_prime(n, k):
    # Write n - 1 as 2^r * d
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    print('d=%d \n r=%d' % (d, r))
    for i in range(0, k):       # WitnessLoop
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(0, r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return 'composite'
            if x == n - 1:
                continue
        return 'composite'
    return 'probably prime'

# Returns 'composite' which is false
print('Prime is: %s' % is_prime(669483106578092405936560831017556154622901950048903016651289, 10))
