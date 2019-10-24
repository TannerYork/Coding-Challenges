# Largest Prime Factor Problem from ProjectEuler.net #

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def largest_prime_factor(number):
    number_sqrt = math.floor(math.sqrt(number))
    numbers = list(range(2, number_sqrt))
    factors = []
    for numb in numbers:
        if number % numb == 0:
            factors.append(numb)
    prime_factors = []
    for factor in factors:
        for numb in range(2, factor):
            if factor % numb == 0:
                break
        else:
            prime_factors.append(factor)

    print('Largest Prime Factor:', max(prime_factors))


# 13195
# 600851475143
largest_prime_factor(600851475143)