def find_kth_largest(nums, k):
    
    nums.sort(reverse=True)
    
    
    if 1 <= k <= len(nums):
        return nums[k - 1]
    else:
        return None 


nums = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3

kth_largest = find_kth_largest(nums, k)

if kth_largest is not None:
    print(f"The {k}-th largest element is {kth_largest}")
else:
    print(f"Invalid value of k.")
