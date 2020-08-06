# Pancake Sort LeepCode #

# Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length,
# then reverse the order of the first k elements of A.  We want to perform zero or more pancake
# flips (doing them one after another in succession) to sort the array A.

# Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer
# that sorts the array within 10 * A.length flips will be judged as correct.

def flip(arr, k):
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]


def pancake_sort(A):
    n = len(A)
    res = []
    for i in range(n):
        j = A.index(max(A[:n-i]))
        flip(A, j+1)
        res.append(j+1)
        flip(A, n-i)
        res.append(n-i)
    return res


def is_sorted(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


if __name__ == "__main__":
    nums = [5, 2, 3, 4, 1]
    print(pancake_sort(nums))
    print(nums)
    assert is_sorted(nums) is True
