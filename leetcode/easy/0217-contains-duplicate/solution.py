class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hs = set()

        for x in nums:
            if x in hs:
                return True
            hs.add(x)

        return False
        