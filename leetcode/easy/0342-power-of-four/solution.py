class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return False

        cnt = 0

        while n & 1 == 0:
            cnt += 1
            n = n >> 1
        
        if n == 1 and cnt % 2 == 0:
            return True
        return False