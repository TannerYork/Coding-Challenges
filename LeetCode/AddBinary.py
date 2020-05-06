# Add Binary #

# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.


## Solution ##
# The solustion below runs in O(n) time where n is the length of the binary
# string with the most digits
def addBinary(a, b):
    smallest = a if len(a) < len(b) else b
    largest = b if len(b) > len(a) else a
    l_i, s_i = len(largest)-1, len(smallest)-1
    remainder = 0
    result = []

    for i in range(s_i, -1, -1):
        total = int(largest[l_i]) + int(smallest[i]) + remainder
        remainder, total = check_binary_total(total)
        result.append(str(total))
        l_i -= 1

    for i in range(l_i, -1, -1):
        total = int(largest[i]) + remainder
        remainder, total = check_binary_total(total)
        result.append(str(total))

    if remainder is not 0:
        result.append(str(remainder))
    return ''.join(reversed(result))


def check_binary_total(binary_total):
    if binary_total is 2:
        return 1, 0
    elif binary_total is 3:
        return 1, 1
    else:
        return 0, binary_total


print(addBinary('11', '1'))  # "100"
print(addBinary('110', '101'))  # "1011"
