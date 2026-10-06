class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        S = {}
        T = {}
        for i in range(len(s)):
            S[s[i]] = i
            T[t[i]] = i

        sm = 0
        for k,v in S.items():
            sm += abs(v - T[k])

        return sm