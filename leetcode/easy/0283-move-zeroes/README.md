# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

Original
Python3
 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 35.50%)  
**Memory:** 20.2 MB (beats 89.62%)  
**Submitted:** 2026-11-15T12:22:37.509Z  

```py
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0 
        j = 0

        while i < len(nums):

            if nums[i] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                j += 1
            i += 1
        return nums
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)