# Single Number LeetCode problem #

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

def singleNumber(nums):
    output = nums[0]
    for index in range(1, len(nums)):
        output = output ^ nums[index]
    return output

if __name__ == '__main__':
    print(singleNumber([2, 2, 1]), 1)
    print(singleNumber([4,1,2,1,2]), 4)