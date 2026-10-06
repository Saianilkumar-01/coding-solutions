class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        cnt = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in cnt:
                cnt[sorted_nums[i]] = i
        
        ans = []
        for x in nums:
            ans.append(cnt[x])
        return ans