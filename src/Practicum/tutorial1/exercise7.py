def get_divisors(a):
    return [x for x in range(1, a + 1) if a % x == 0]


def is_prime(n):
    return len(get_divisors(n)) == 2


def get_prime_factorization(a):
    factorization = []
    temp = a
    prime_divisors = [x for x in get_divisors(a) if len(get_divisors(x)) == 2]
    for prime in prime_divisors:
        while temp % prime == 0:
            temp /= prime
            factorization.append(prime)
    return factorization


if __name__ == '__main__':
    print('Divisors of 12: ' + str(get_divisors(2)))
    print('Prime factorization of 360 is: %s' % get_prime_factorization(360))
