# Second Largest

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of positive integers  **arr[]**, return the second largest element from the array. If the second largest element doesn't exist then return  **-1.** 

Note: The second largest element should not be equal to the largest element.

 **Examples:** 

```
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
```

```
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
```

```
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-25T07:01:48.363Z  

```py
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
                
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/second-largest3735/1)