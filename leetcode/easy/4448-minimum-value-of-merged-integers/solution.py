class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:

        mn = float('inf')

        for i in range(0,len(nums),2):
            x = int(str(nums[i]) + str(nums[i+1]))
            mn = min(mn,x)
        return mn