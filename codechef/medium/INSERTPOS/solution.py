class Solution:
    def search_insert_position(self, arr, target):
        # write your code here
        
        low = 0
        high = len(arr)
        
        while low < high:
            
            mid = ( low + high ) // 2
            
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid 
        
        return low