# Roman Numeral to Decimal problem from CTI-ISP-2020 #

# Given a roman numeral, convert it to an integer. Input is guaranteed to be
#  within the range from 1 to 3999.

char_to_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman_to_decimal(roman_numeral):
  if len(roman_numeral) == 1:
    return char_to_num[roman_numeral]

  total = 0 
  for i in range(len(roman_numeral)-1, -1, -1):
    value = char_to_num[roman_numeral[i]]
    prev_value = char_to_num[roman_numeral[i+1]] if i < len(roman_numeral)-1 else 0
    if value >= prev_value:
      total += value
    else:
      total -= value
  return total
  
#### Pesudocode ####
# Create a way to determin a single characters number
  # Comparing a character to a dictionary of character, number pairs

# Iterate over the characters in the given roman numeral bacwards
 # Get the current characters numerical value
 # if the value is creater than the previous value, add it to the total
 # else if the value is less than, subtract if from the total
# Return the total value

#### Walkthrough ####
# XLIV <---
# V = 5
# IV = 5 - 1 = 4
# LIV = 4 + 50 = 54
# XLIV = 54 - 10 = 44

#### Testing ####
roman = input('Enter roman numeral:')
print(roman_to_decimal(roman))