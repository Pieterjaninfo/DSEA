# Returns a list with all the fibonnaci numbers whos values do not exceed n
def get_fib(n):
    fib = [0, 1]
    i = 2
    while True:
        value = fib[i - 1] + fib[i - 2]
        if value >= n:
            return fib
        fib.append(value)
        i += 1


def get_sum_even_fib(fib):
    return sum([x for x in fib if x % 2 == 0])


print('Sum of all even fib numbers under 4million: %d' % get_sum_even_fib(get_fib(4000000)))
