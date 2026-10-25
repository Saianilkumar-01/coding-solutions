class Solution:
    def missingNum(self, arr):
        # code here
        mx = max(arr)
        
        sm = sum(arr)
        s = mx * (mx + 1) // 2
        if sm  == s:
            return mx + 1
        return s - sm