class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = -1
        second_largest = -1
        
        for x in arr:
            
            if x > largest:
                second_largest = largest
                largest = x
            elif x > second_largest and largest != x:
                second_largest = x
        return second_largest
                