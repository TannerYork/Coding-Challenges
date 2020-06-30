# String to Integer (atoi) LeetCode problem #

# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace 
# character is found. Then, starting from this character, takes an optional initial plus or minus sign 
# followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are 
# ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such
# sequence exists because either str is empty or it contains only whitespace characters, no conversion is
# performed.
# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
# range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

def myAtoi(str):
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    output_num = []
    first_proper_char_found, found_sign = False, False
    for i in range(len(str)):
        if not first_proper_char_found:
            if str[i] in '+-' or str[i].isnumeric() or str[i] == '.':
                output_num.append(str[i])
                first_proper_char_found = True
            if not first_proper_char_found and not str[i].isnumeric() and str[i] != ' ':
                return 0
        else:
            if not str[i].isnumeric(): break
            output_num.append(str[i])

    # Check that output_num is valid
    only_digits = [s for s in output_num if s.isnumeric()]
    if len(output_num) == 0: 
        return 0
    if len(only_digits) == 0:
        return 0

    # Check output_num is in 32bit range 
    output_num = int(float(''.join(output_num)))
    if output_num > INT_MAX:
        return INT_MAX
    if output_num < INT_MIN:
        return INT_MIN
    return output_num


if __name__ == '__main__':
    print(myAtoi('words in front of number 90'), 0)
    print(myAtoi('90 in front of words'), 90)
    print(myAtoi("  -0012a42"), -12)
    print(myAtoi('+'), 0)
    print(myAtoi("   +0 123"), 0)