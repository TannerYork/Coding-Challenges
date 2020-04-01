# Largest Substring Without Repeating Characters#

# Given a string, find the length of the longest substring without repeating characters.


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest, index, count, sub_string = 0, 0, 0, set()
    while count != len(s) and index != len(s):
        if s[count] in sub_string:
            if len(sub_string) > longest:
                longest = len(sub_string)
            index += 1
            sub_string, count = set(), index
        else:
            sub_string.add(s[count])
            count += 1
    return longest if len(sub_string) < longest else len(sub_string)


solution = lengthOfLongestSubstring("abcacdbb")
print(solution)
