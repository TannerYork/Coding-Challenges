# Valid Anagram #

# Given two strings s and t , write a function to determine if t is an anagram of s. #

## Solution ##
# The overall time complexity of this solution is O(n log n ) becase assuming n is the
#  length of s, sorting s take O(n log n) time while comparing the two only takes O(n) time.
# The space complexity of this solution is O(1) because the sorting and comparision is in-place.


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s.sort()
    t.sort()
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True
