class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = s2 = 0

        while a > 0:
            if a & 1 == 1:
                s1 += 1
            a = a // 2
        while b > 0:
            if b & 1 == 1:
                s2 += 1
            b = b // 2

        return s1 * s2 if s1 >= s2 else s2 // s1