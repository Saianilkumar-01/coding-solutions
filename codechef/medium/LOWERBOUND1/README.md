# LOWERBOUND1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T13:49:55.843Z  

```py
def search_insert_position(arr, n, k):
    # Write your code here
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            l = mid+ 1
        else:
            h = mid - 1
    else:
        return l
```

---

[View on CodeChef](https://www.codechef.com/problems/LOWERBOUND1)