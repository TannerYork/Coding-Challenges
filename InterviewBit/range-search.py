# Search for Range CTI-ISP 2020 #

# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

def binary_search(arr, start, end, target):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, start, mid-1, target)
        else:
            return binary_search(arr, mid + 1, end, target)
    else:
        return -1


def search_for_range(array, target):
    target_index = binary_search(array, 0, len(array)-1, target)
    if target_index == -1:
        return [-1, -1]
    start, end = target_index, target_index
    while array[start-1] == target and start >= 1:
        start -= 1
    while end < len(array)-1 and array[end+1] == target:
        end += 1

    return [start, end]


if __name__ == '__main__':
    print(search_for_range([5, 7, 7, 8, 8, 10], 8), [3, 4])
    print(search_for_range([8, 8, 8, 8, 8, 8, 8, 8], 8), [0, 7])
    print(search_for_range([8, 8], 8), [0, 1])
    print(search_for_range([7, 7, 7, 7, 7], 8), [-1, -1])
