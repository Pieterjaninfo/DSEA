import itertools

def get_palindrome():
    max_num = 0
    max_pair = (0,0)
    for i, j in itertools.product(range(100, 1000), range(100, 1000)):
        value = i*j
        if str(value) == str(value)[::-1]:
            if value > max_num:
                max_num = value
                max_pair = (i,j)
    return max_num

# print(get_palindrome())
print('Largest palindrome made from product of two 3-digit numbers is: %d' % get_palindrome())
