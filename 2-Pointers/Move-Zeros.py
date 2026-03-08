# Original Idea
def moveZeroes(nums):
    l = 0
    r = len(nums)
    stack = []
    zero_count = 0

    for i, num in enumerate(nums):
        if num == 0:
            stack.append(i)
            zero_count += 1
    
    while stack:
        index = stack.pop()
        nums.pop(index)
    
    nums.extend([0] * zero_count)

# Optimised solution
def moveZerosOptimised(nums):
    n = len(nums)
    list2 = [0] * n
    index = 0
    for i in range(n):
        if nums[i] != 0:
            list2[index] = nums[i]
            index += 1
    nums[:] = list2

moveZerosOptimised([2,0,4,0,9])
moveZerosOptimised([0,0,1])