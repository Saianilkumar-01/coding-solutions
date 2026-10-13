class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = float("-inf")

        max2 = float("-inf")

        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x

        return (max1-1)*(max2-1)