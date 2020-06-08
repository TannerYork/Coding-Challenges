# Smallest Multiple problem from Project Euler #

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# I know you can solving this problem with pure math but what's the fun in that?
def find_smallest_multiple(num):
    current_number = num
    while True:
        is_multiple = True
        for i in range(num, 1, -1):
            if current_number % i != 0:
                is_multiple = False
        if is_multiple:
            return current_number
        current_number += 10


if __name__ == '__main__':
    print(find_smallest_multiple(20))
