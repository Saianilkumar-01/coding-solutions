def upper_bound(nums, x):
    # write code here...
    
    low = 0
    high = len(nums) - 1
    ans = low
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if nums[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans