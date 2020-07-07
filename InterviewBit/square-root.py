# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# Do not use any built square root functions.

def squareRoot(num):
    low, high, mid = 0.0, float(num), -1
    for _ in range(1000):
        mid = (low + high) / 2.0
        if mid**2 == num:
            return int(mid)
        if mid**2 > num:
            high = mid
        else:
            low = mid
    return int(mid)


if __name__ == '__main__':
    print(squareRoot(9), 3)
    print(squareRoot(11), 3)
    print(squareRoot(1020011), 1009)
