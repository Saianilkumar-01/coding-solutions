# Maximum Product of Two Elements in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array of integers `nums`.

Choose two  **different**  indices `i` and `j` of that array.

Return the  **maximum**  value of `(nums[i] - 1) * (nums[j] - 1)`.

 

 **Example 1:** 

```
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1) *(nums[2]-1) = (4-1)* (5-1) = 3*4 = 12. 

```

 **Example 2:** 

```
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

```

 **Example 3:** 

```
Input: nums = [3,7]
Output: 12

```

 

 **Constraints:** 

- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^3

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.1 MB  
**Submitted:** 2026-10-13T15:57:24.515Z  

```py
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = float("-inf")

        max2 = float("-inf")

        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x

        return (max1-1)*(max2-1)
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)