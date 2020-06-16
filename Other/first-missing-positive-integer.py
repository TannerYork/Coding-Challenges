# First Missing Positive Integer from CTI-ISP-2020 #

# Given an unsorted integer array, find the first missing positive integer.
# Solution should be in O(n) time complexity


def first_missing_positive_integer(integers):
  numb_range = []
  for integer in integers:
    if integer < 0:
      continue
    if integer > len(numb_range):
      numb_range.extend([False] * (integer - len(numb_range)))
    numb_range[integer-1] = True
  
  missing_numb = -1
  for i in range(len(numb_range)):
    if numb_range[i] == False:
      return i + 1
  if missing_numb == -1:
    missing_numb = len(numb_range)+1
  return missing_numb
  
result = first_missing_positive_integer([1,3,4,5,6,7,8,9]) # 2
print(result)