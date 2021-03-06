# Fibonacci Even Numbers Problem from ProjectEuler.net #

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.


limit = 4000000
count = 0
x = 1
y = 2
z = 0
total = 2

while total < limit:
    count = x + y
    z = x
    x = y
    y = count
    if count % 2 == 0:
        total += count

if count > limit:
    count -= z
    total -= count

print(total)