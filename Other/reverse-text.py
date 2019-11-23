# Reverse text problem form Ryan Hopkins #

# Revese a given set of text


### SOLUTION ###
# The solution below has a time complexity of O(n) and a space complexity of O(1).

def reverse_text(text_array):
    # Iterate through the text swapping the first value with the last, the second 
    # value with the second to last... untill the text is reversed.
    for index in range(len(text_array)//2):
        text_array[index], text_array[(len(text_array)-1)-index] = \
        text_array[(len(text_array)-1)-index], text_array[index]


### TESTING ###
text_array = ['THIS', 'IS', 'A', 'STRING']
print(text_array)
reverse_text(text_array)
print(text_array)