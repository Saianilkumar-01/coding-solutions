# Trapping Rain Water

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

 **Example 1:** 

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

 **Example 2:** 

```
Input: height = [4,2,0,3,2,5]
Output: 9

```

 

 **Constraints:** 

- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 43.36%)  
**Memory:** 21.1 MB (beats 50.62%)  
**Submitted:** 2026-10-08T16:43:38.417Z  

```py
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        lmax = [0]*len(height)
        rmax = [0]*len(height)

        lmax[0] = height[0]
        rmax[-1] = height[-1]

        for i in range(1,n):
            lmax[i] = max(lmax[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            rmax[i] = max(rmax[i+1] , height[i])

        sm = 0
        for i in range(n):
            sm += (min(lmax[i],rmax[i]) - height[i])

        return sm 
```

---

[View on LeetCode](https://leetcode.com/problems/trapping-rain-water/)