# Merge Sort: Counting Inversions HackerRank problem #

# In an array, arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. 
# In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". To correct an 
# inversion, we can swap adjacent elements.

# Complete the function countInversions in the editor below. It must return an integer representing
#  the number of inversions required to sort the array.
# countInversions has the following parameter(s):
#       arr: an array of integers to sort .

def merge(arr1, arr2, inversions):
    merged_arr = []
    i1, i2 = 0, 0
    while(len(arr1) > i1 and len(arr2) > i2):
        if arr1[i1] <= arr2[i2]:
            merged_arr.append(arr1[i1])
            i1 += 1
        else:
            inversions += len(arr1)-i1
            merged_arr.append(arr2[i2])
            i2 += 1
    if len(arr1) > i1:
        merged_arr += arr1[i1:]
    elif len(arr2) > i2:
        merged_arr += arr2[i2:]
    return merged_arr, inversions

def merge_sort(arr):
    if (len(arr) == 1):
        return arr, 0
    mid = len(arr)//2
    left, left_inversions = merge_sort(arr[:mid])
    right, right_inversions = merge_sort(arr[mid:])
    return merge(left, right, left_inversions + right_inversions)
    
# Complete the countInversions function below.
def countInversions(arr):
    """Merge sort the arr and for every intersion add to the counter"""
    new_array, inversions = merge_sort(arr)
    return inversions


if __name__ == '__main__':
    print(countInversions([1, 1, 1, 2, 2]), 0)
    print(countInversions([2, 1, 3, 1, 2]), 4)

    print(countInversions([1, 5, 3, 7]), 1)
    print(countInversions([7, 5, 3, 1]), 6)