# Find the largest palidrame substring from Ryan Hopkins #

# Given a n lengthed string find the largest palindrome substring in the string


def largest_palindrome(string, last_lp=""):
    if len(string) <= len(last_lp):
        return last_lp
    elif string == string[::-1] and len(string) > len(last_lp):
        last_lp = string
    P1 = largest_palindrome(string[:-1], last_lp)
    P2 = largest_palindrome(string[1:], last_lp)
    return P1 if len(P1) > len(P2) else P2

print(largest_palindrome('aracecar')) # racecar