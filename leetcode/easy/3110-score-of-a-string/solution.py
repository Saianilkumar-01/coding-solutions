class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            sm = abs(ord(s[i]) - ord(s[i+1]))
            ans += sm

        return ans