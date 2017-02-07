import itertools
from math import sqrt

# Prime Sieve of Eratosthenes
def prime_sieve(n):
    is_composite = [False] * n
    print(is_composite)
    return


    primes = []
    for m in range(2, n + 1):
        if not is_composite[m]:
            primes.append(m)

            k = 2
            while k * m < n:
                print('k * m = %d * %d = %d  length: %d' % (k, m, k * m, len(is_composite)))
                is_composite[k * m] = True
                k += 1
        else:
            print('%d is composite number' % m)     # It is a composite number, do nothing?
    return primes


# def prime_sieve(n):
#     A = [True] * (n - 1)
#     primes = []
#
#     for i in range(2, int(sqrt(n))):
#         if A[i]:
#             primes.append(i)
#
#             j = i * i
#             while j < n:
#                 A[j] = False
#                 j += i
#
#     # return [x + 2 for x in range(0, n - 1) if A[x]]
#     return primes

print(prime_sieve(10))
