# Least Changes For Anagram Problem from HackerRank.com #

# Given a function that takes in two strings with any character, return 
# the number of changes needed to make the second string an anagram of the first

def get_changes_for_anagram(string1, string2):
    count = 0 
    character_count = {}

    if len(string1) != len(string2):
        return -1

    for char in string1:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    for char in string2:
        if char in character_count:
            character_count[char] -= 1
            if character_count[char] == 0:
                del character_count[char]
        else:
            count += 1
    return count
          
a = 'ssit'
b = 'ssrj'

print(get_changes_for_anagram(a,b))