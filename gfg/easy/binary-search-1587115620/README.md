# First Occurrence in Sorted

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array  **arr[]**  and an integer  **k**, find the position(0-based indexing) at which k is present in the array using binary search. If k doesn't exist in arr[] return  **-1**. 

 **Note:**  If multiple occurrences are there, please return the smallest index.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 5], k = 4
Output: 3
Explanation: 4 appears at index 3.
```

```
Input: arr[] = [11, 22, 33, 44, 55], k = 445
Output: -1
Explanation: 445 is not present.

```

```
Input: arr[] = [1, 1, 1, 1, 2], k = 1
Output: 0
Explanation: 1 appears at index 0.
```

**Constraints:
**1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106
1 ≤ k ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-26T02:36:51.919Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/binary-search-1587115620/1)