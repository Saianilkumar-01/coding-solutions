class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        S = {}
        T = {}
        for i in range(len(s)):
            S[s[i]] = S.get(s[i],0)+i
        for j in range(len(t)):
            T[t[j]] = T.get(t[j],0)+j

        sm = 0
        for x in s:
            sm += abs(T[x] - S[x])

        return sm