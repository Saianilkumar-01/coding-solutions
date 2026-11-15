class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k <= -1:
            return -1

        #revesre whole array
        i = 0 
        j = len(nums)-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        k = k % len(nums)
        
        #revesre upto kth index
        i = 0
        j = k - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        
        #reverse from kth index
        i = k
        j = len(nums)-1
        while i < j:
            nums[i] , nums[j] = nums[j] , nums[i]
            i += 1
            j -= 1

        return nums