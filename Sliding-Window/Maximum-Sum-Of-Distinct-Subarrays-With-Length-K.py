from collections import defaultdict
def maximumSubarraySum(nums, k):
    # the max_count to return
    max_count = float("-inf")
    # A set to keep track of elements in the substring
    num_count = defaultdict(int)
    # A current count of the substring sum 
    subarray_count = 0
    # A left pointer, which points to the beginning of the subarray
    l = 0
    for r in range(len(nums)):
        subarray_count += nums[r]
        num_count[nums[r]] += 1
        if r - l + 1 == k:
            if len(num_count) == k:
                max_count = max(subarray_count, max_count)
                subarray_count -= nums[l]
                del num_count[nums[l]]
                l += 1
            else:
                num_count[nums[l]] -= 1
                subarray_count -= nums[l]
                if num_count[nums[l]] == 0:
                    del num_count[nums[l]]
                l += 1

    return max(0, max_count)