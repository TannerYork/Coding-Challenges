def isPowerOfThree(n):
    if n == 0:
        return False
    if n == 1:
        return True

    current_num = n
    while current_num != 3:
        current_num /= 3
        if current_num % 3 != 0:
            return False
    return True


if __name__ == '__main__':
    print(isPowerOfThree(19684))
    print(isPowerOfThree(27))
