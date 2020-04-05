# Two Sum #

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twoSum(nums, target):
    nums = sorted(enumerate(nums), key=lambda x: x[1])
    i, j = 0, len(nums)-1
    count = nums[i][1] + nums[j][1]
    while i < j and count != target:
        if count < target:
            i += 1
        else:
            j -= 1
        count = nums[i][1] + nums[j][1]
    return [nums[i][0], nums[j][0]]


print(twoSum([3, 2, 4], 6))
