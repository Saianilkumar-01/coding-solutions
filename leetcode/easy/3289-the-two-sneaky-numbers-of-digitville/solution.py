class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []
        for x in nums:
            hm[x] = hm.get(x,0)+1

            if hm[x] == 2:
                res.append(x)

        return res