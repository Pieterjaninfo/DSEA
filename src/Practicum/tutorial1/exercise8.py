def get_divisors(a):
    divs = [1]
    i = 2
    while i * i <= a:
        if a % i == 0:
            divs.append(i)
        i += 1
    divs.append(a)
    return divs


def get_largest_primefactor(n):
    result = 1
    divs = [x for x in get_divisors(n) if len(get_divisors(x)) == 2]

    for prime_factor in divs[::-1]:
        result = max(result, prime_factor)
    return result


print('Largest prime factor of 13195: %d' % get_largest_primefactor(13195))
print('Largest prime factor of 600851475143: %d' % get_largest_primefactor(600851475143))
