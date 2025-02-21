def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    else:
        nums.sort()
        return nums[1]
    
nums1 = [3, 2, 1, 4]
print(goldilocks_approved(nums1))

nums2 = [1, 2]
print(goldilocks_approved(nums2))

nums3 = [2, 1, 3]
print(goldilocks_approved(nums3))

