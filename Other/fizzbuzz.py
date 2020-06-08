# Fizzbuzz problem from CTI-ISP-2020 (Intervew Problem Solving) #

# Given an input, print all numbers up to and including that input,
# unless they are divisible by 3, then print "fizz" instead, or if
# they are divisible by 5, print "buzz". If the number is divisible
# by both, print "fizzbuzz".

# Example Given 15:
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz


def fizzbuzz(n):
    for number in range(1, n+1):  # range is not inclusive at the end
        if number % 3 == 0 and number % 5 == 0:
            print('fizzbuzz')
        elif number % 3 == 0:
            print('fizz')
        elif number % 5 == 0:
            print('buzz')
        else:
            print(number)


if __name__ == '__main__':
    test_case = int(input("Please enter an input number:"))
    fizzbuzz(test_case)
