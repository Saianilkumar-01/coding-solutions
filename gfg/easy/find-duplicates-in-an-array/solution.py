class Solution:
    def findDuplicates(self, arr):
        # code here
        hm = {}
        res =[]
        for x in arr:
            hm[x] = hm.get(x,0)+1
            
            if hm[x] == 2:
                res.append(x)
                
        return res