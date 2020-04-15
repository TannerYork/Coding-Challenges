# Matching/Balanced Brackets Problem from Exercism.io #

# Given a string containing brackets [], braces {}, parentheses (),
#  or any combination thereof, verify that any and all pairs are
# matched and nested correctly.


def is_paired(input_string):
    open_brackets = set(['{', '(', '['])
    closing_brackets = set(['}', ')', ']'])
    opposite = {'}': '{', ')': '(', ']': '['}
    stack = []

    for char in input_string:
        if char in open_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if opposite[char] != top:
                return False
    return True if len(stack) == 0 else False


# Basic Test
print(is_paired('{[]}'), True)
print(is_paired('{[}]'), False)

# Edge Cases Test
print(is_paired('{{{{{{{}}}}}}}'), True)
print(is_paired('[([([()])])]'), True)
print(is_paired('[  ]'), True)
