# Repeated Strings #

# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's
#  infinite string.

import math


def repeatedString(s, n):
    num_a = s.count('a')
    num_full_s = math.floor(n / len(s))
    char_left = n - (num_full_s * len(s))

    num_a *= num_full_s
    for index in range(char_left):
        if s[index] is 'a':
            num_a += 1
    return num_a


if __name__ == '__main__':
    print(repeatedString('aba', 10), 7)
    print(repeatedString('a', 1000000000000), 1000000000000)
