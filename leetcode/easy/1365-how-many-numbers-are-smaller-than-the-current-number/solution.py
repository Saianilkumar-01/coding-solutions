class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i] and i != j:
                    ans[i] += 1
        return ans