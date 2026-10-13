class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hm = {}

        for x in nums:
            hm[x] = hm.get(x,0)+1

        for x in nums:
            if hm[x] == 1:
                return x