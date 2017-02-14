def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


print('GCD(3141,156)= %d' % gcd(3141, 156))
print('gcd(12345678, 987654321)= %d' % gcd(12345678, 987654321)) # 9x9 square tiles


def frac(a, b):
    if b == 0:
        return
    scale = gcd(a, b)
    return (a//scale),(b//scale)


res = frac(65457, 8)
print('FRAC: %d/%d' % (res[0], res[1]))
print('GCD(%d/%d)=%d' % (res[0], res[1], gcd(res[0], res[1])))


def extended_gcd(a, b):
    s = 0
    t = 1
    r = b
    old_s = 1
    old_t = 0
    old_r = a

    while r != 0:
        quotient = old_r % r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    print('Bézout coefficients: %d, %d' % (old_s, old_t))
    print('greatest common divisor: %d' % old_r)
    print('quotients by the gcd: %d, %d' % (t, s))

extended_gcd(5, 10)