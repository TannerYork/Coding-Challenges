# K Frequent Words #

# Given a string of text and a number k, find the k words in the given text that appear
# most frequently. Return the words in a new array sorted in decreasing order.


def k_frequent_words(text, k):
    text = text.split()
    word_counts = {}

    for word in text:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    
    # Old version that makes the function O(jlogj) where j is the number of individual words
    # key_values = list(zip(word_counts.values(), word_counts.keys()))
    # key_values.sort(reverse=True)

    # words = []
    # for i in range(k):
    #     words.append(key_values[i][1])
    # return words

    # New version that makes the function O(j**2) where j is the number of individual words
    output = []
    for i in range(k):
        max_value = max(word_counts, key=lambda x: word_counts[x])
        del word_counts[max_value]
        output.append(max_value)
    return output



most_frequent = k_frequent_words('two two three two five six six four four', 2)
print(most_frequent)
