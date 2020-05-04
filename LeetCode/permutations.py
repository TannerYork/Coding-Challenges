# Permutations #

# Given a collection of distinct integers, return all possible permutations.


# This algorithms time complexity is O(n^2)
def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    permutes = []
    for i in range(len(nums)):  # O(n)
        m = nums[i]
        remLst = nums[:i] + nums[i+1:]

        for p in permute(remLst):  # O(n)
            permutes.append([m] + p)
    return permutes


assert permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [
    2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
assert permute([1, 2, 3, 4]) == [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [
    2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
