encode_list = list('0123456789abcdefghijklmnopqrstuvwxyz')


def encode(n):
    return encode_list[n]


# n > 0 and  2 <= k <= 35
def to_k(n, k):
    result = ''
    temp = n
    while temp != 0:
        result += (encode(temp % k))
        temp //= k
    return result[::-1]


def decode(string):
    return encode_list.index(string)


def from_k(s, k):
    return sum([decode(x) * pow(k, len(s) - idx - 1) for idx, x in enumerate(s)])


def convert(k, m, s):
    return to_k(from_k(s, k), m)


print('Encodings 0:%s 8:%s 35:%s' % (encode(0), encode(8), encode(35)))
print('to_k(4321,16)= %s' % to_k(4321, 16))
print('Decodings 0:%d 8:%d z:%d' % (decode('0'), decode('8'), decode('z')))
print('from_k(10e1,16) = %d' % from_k('10e1', 16))
print('convert(2, 4, 10011010)=%s' % convert(2, 4, '10011010'))
print('convert(16, 7, B48C03)=%s' % convert(16, 7, 'b48c03'))
