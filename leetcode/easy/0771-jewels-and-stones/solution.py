class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        i = 0
        sm = 0
        while i < len(jewels):
            j = 0
            while j < len(stones):
                if jewels[i] == stones[j]:
                    sm += 1
                j += 1
            i += 1
        return sm