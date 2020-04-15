# Two Sum #

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twoSum(nums, target):
    diff = set()
    for num in nums:
        if target - num in diff:
            return [num, target-num]
        else:
            diff.add(num)
    return []


print(twoSum([3, 2, 4], 6))
print(twoSum([49, -3, 50, 37, 41], 34))
