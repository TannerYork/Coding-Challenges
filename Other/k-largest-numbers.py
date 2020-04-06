# K Largest Numbers #

# Find the k largest numbers in a an array of n numbers.
# Return them in an array sorted in decreasing order.


def k_largest(arr, k):
    # Time complexity O(n log(n)), given the sorting function is O(n log(n)).
    if k == len(arr):
        return arr
    if k > len(arr):
        return None

    arr.sort(reverse=True)
    largest = []
    for i in range(k):
        current_index = i
        largest.append(arr[current_index])
    return largest


input1 = [2, 6, 4, 20, 5, 43]
input2 = [2, 6, -4, 20, -5, 43, -100, 100, 50, 43]
print(k_largest(input1, 3))
print(k_largest(input2, 5))
