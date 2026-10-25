class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        array = nums[:]

        total = sum(nums)
        gain = []

        for num in array:
            x = sorted(str(num),reverse=True)
            new_x = int("".join(x))

            g = new_x - num
            gain.append(g)

        gain.sort(reverse=True)

        for i in range(k):
            total += gain[i]

        return total