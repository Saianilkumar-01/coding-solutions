class Solution:
    def reverseDegree(self, s: str) -> int:
        sm = 0

        for i in range(len(s)):

            degree = 26 - (ord(s[i]) - ord('a'))
            sm += degree * ( i + 1)
        return sm