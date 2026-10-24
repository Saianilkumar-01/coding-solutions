class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        cnt = 0
        lenght = 0

        for num in nums:

            if minK <= num <= maxK:
                lenght += 1
                cnt += lenght
            else:
                lenght = 0

        return cnt