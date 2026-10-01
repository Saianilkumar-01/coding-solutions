class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        res = [0] * (len(encoded) + 1)
        res[0] = first

        for i in range(len(encoded)):
            res[i+1] = res[i] ^ encoded[i]
        return res