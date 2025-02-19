
def non_decreasing(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count += 1
            if count > 1: 
                print("False")
                return
    print("True")
    
    
nums1 = [4, 2, 3]
non_decreasing(nums1)

nums2 = [4, 2, 1]
non_decreasing(nums2)