# Length Of Last Word from IntervewBit #

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#  return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.

def length_of_last_word(words):
    found_space, count = True, 0
    for i in range(len(words)):
        if found_space and words[i].isalpha():
            count = 1
        elif not found_space and words[i].isalpha():
            count += 1
        found_space = (words[i] == ' ')
    return count


if __name__ == '__main__':
    print(length_of_last_word("Hello World"), 5)
    print(length_of_last_word("bbbb aaaa ccccc b"), 1)
    print(length_of_last_word('            '), 0)
