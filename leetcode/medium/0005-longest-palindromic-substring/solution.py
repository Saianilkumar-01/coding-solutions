class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        for i in range(len(s)):
            for j in range(i,len(s)):
                ch = s[i:j+1]
                if ch == ch[::-1]:
                    if len(res) < len(ch):
                        res = ch

        return res