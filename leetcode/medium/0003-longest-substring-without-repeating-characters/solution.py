class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        ans = 0

        for x in range(len(s)):

            if s[x] in hm:
                l = max(l,hm[s[x]]+1)

            hm[s[x]] = x
            ans = max(ans,x-l+1)
        return ans