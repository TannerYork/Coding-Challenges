# Longest Plaindrom from LeetCode #

# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

def longest_palindrome(input_string):
    tmp = ""
    for i in range(len(input_string)):
        odd = expandPalindorome(input_string, i, i)
        even = expandPalindorome(input_string, i, i+1)
        tmp = max(tmp, odd, even, key=len)
    return tmp.strip()


def expandPalindorome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


if __name__ == '__main__':
    print(longest_palindrome('babad'), '== bab or aba')
    print(longest_palindrome('I want a racecar for my birthday'), '== racecar')
    print(longest_palindrome('cb'), '== c or b')
