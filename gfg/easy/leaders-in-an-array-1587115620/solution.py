class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        right_mx = float('-inf')
        
        ans = []
        
        for i in range(n-1,-1,-1):
            
            if arr[i] >= right_mx:
                ans.append(arr[i])
                right_mx = arr[i]
                
        return ans[::-1]