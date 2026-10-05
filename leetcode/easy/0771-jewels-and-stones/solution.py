class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        sm = 0
        for x in stones:
            if x in jewels:
                sm += 1
        return sm