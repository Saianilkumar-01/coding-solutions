class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {}
        c = {}
        vowels = ['a','e','i','o','u']
        for x in s:
            if x in vowels:
                v[x] = v.get(x,0)+1
            else:
                c[x] = c.get(x,0)+1
        return max(v.values(),default= 0) + max(c.values(),default= 0)