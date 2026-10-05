class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        hm = set(nums)
        i = min(nums)
        ans = []
        while i <= max(nums):
            if i not in hm:
                ans.append(i)
            i += 1
        return ans