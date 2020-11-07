# Sum Square Difference from Project Euler #

# The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is.
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(n):
    sum_of_squares = 0
    for i in range(n + 1):
        sum_of_squares += i**2

    sum_squared = 0
    for i in range(n + 1):
        sum_squared += i
    sum_squared = sum_squared**2

    return sum_squared - sum_of_squares


if __name__ == '__main__':
    print(sum_square_difference(100))