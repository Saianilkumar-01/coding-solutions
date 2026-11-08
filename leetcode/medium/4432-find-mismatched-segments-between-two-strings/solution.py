class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res =[]
        i = 0 
        n = len(s1)

        while i < n:
            if s1[i] == s2[i]:
                i += 1
            else:
                st = i

                while i < n and s1[i] != s2[i]:
                    i += 1

                res.append([s1[st:i] , s2[st:i]])
        return res