class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_length = 1
        start = 0

        for i in range(len(s)):
            p1 = i
            p2 = i

            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            length = p2 - p1 - 1
            if length > max_length:
                max_length =  length
                start = p1 + 1
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            length = p2 - p1 -1
            if max_length < length:
                max_length = length
                start = p1 + 1
        return s[start:start+max_length]