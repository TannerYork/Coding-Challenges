# Largest Palindome Product Problem from ProjectEuler.net #

# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

three_diget_range = range(100, 999)

products = []
for index_0 in three_diget_range:
    for index_1 in three_diget_range:
        products.append(index_0 * index_1)

palindomes = []
for product in products:
    string_product = str(product)
    if string_product == ''.join(reversed(string_product)):
        palindomes.append(product)
        
print(max(palindomes))