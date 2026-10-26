class Solution:
    def firstSearch(self, arr, k):
        # Code Here
        p1 = 0
        p2 = len(arr) - 1 
        
        ans = -1
        
        while p1 <= p2:
            
            mid = (p1 + p2) // 2
            
            if arr[mid] == k:
                ans = mid
                p2 = mid - 1
                
            elif arr[mid] < k:
                p1 = mid + 1
            else:
                p2 = mid - 1
                
        return ans