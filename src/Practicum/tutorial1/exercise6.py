def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def binom(n, k):
    return fact(n) / (fact(k) * fact(n-k))

print('fact(28)= %d' % fact(28))

print('binom(12, 8)=%d' % binom(12, 8))
print('binom(40, 2)=%d' % binom(40, 2))
