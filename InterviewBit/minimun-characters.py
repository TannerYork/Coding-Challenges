# Minimum Characters from CTI-ISP 2020 #

# You are given a string. The only operation allowed is to insert characters 
# in the beginning of the string. Return the number of characters that are 
# needed to be inserted to make the string a palindrome string

# Examples:
# Input: ABC
# Output: 2
# Input: AACECAAAA
# Output: 2


def minimumCharacters(string):
  characters = 0
  start, end = 0, len(string)-1
  while start != end:
    if string[start] != string[end]:
      characters += 1
      end -= 1
    else:
      start += 1 
      end -= 1
  return characters
  

if __name__ == '__main__':
    print(minimumCharacters('ABC'), 2)
    print(minimumCharacters('AACECAAAA'), 2)