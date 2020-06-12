# Trailing Zero Factorial from CTI-ISP-2020 # 

# Given an integer n, return the number of trailing zeroes in n!.

# Fast Solution #
def fast_trailing_zero_factorial(n):
  trailing_zeros = 0
  
  # Iterate over the multiples of five
  multiplier = 1
  while True:
    if n < 5*multiplier:
      if n > 24: # 
        trailing_zeros += 1
      return trailing_zeros
    trailing_zeros += 1
    multiplier += 1

# Slow solutions #
def factorial_of(n):
    return 1 if (n==1 or n==0) else n * factorial_of(n - 1);  

def slow_trailing_zero_factorial(n):
  # Get the factorial of a given number
  factorial = factorial_of(n)
  print(factorial_of(n))
  # Count the trailing zeros in the factorial
  trailing_zeros = 0
  fact_str = str(factorial)
  for i in range(len(fact_str)-1, -1, -1):
    if fact_str[i] != '0':
      break
    trailing_zeros += 1
  return trailing_zeros

if __name__ == '__main__':
    print(fast_trailing_zero_factorial(4), '0')
    print(fast_trailing_zero_factorial(5), '1')
    print(fast_trailing_zero_factorial(10), '2')
    print(fast_trailing_zero_factorial(26), '6')
