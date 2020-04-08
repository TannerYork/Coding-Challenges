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
    key_values = list(zip(word_counts.values(), word_counts.keys()))
    key_values.sort(reverse=True)

    words = []
    for i in range(k):
        words.append(key_values[i][1])
    return words


most_frequent = k_frequent_words('two two three two five six six four four', 2)
print(most_frequent)
