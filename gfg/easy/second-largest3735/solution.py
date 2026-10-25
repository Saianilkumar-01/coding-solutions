class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = float('-inf')
        second_largest = float('-inf')
        
        for x in arr:
            
            if x > largest:
                second_largest = largest
                largest = x
            elif x > second_largest and largest != x:
                second_largest = x
        return second_largest if second_largest != float('-inf') else -1
                