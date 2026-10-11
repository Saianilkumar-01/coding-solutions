# Power of Four

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `n`, return  *`true` if it is a power of four. Otherwise, return `false`*.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4x`.

 

 **Example 1:** 

```
Input: n = 16
Output: true

```

 **Example 2:** 

```
Input: n = 5
Output: false

```

 **Example 3:** 

```
Input: n = 1
Output: true

```

 

 **Constraints:** 

- -231 <= n <= 231 - 1

 

 **Follow up:**  Could you solve it without loops/recursion?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 59.72%)  
**Submitted:** 2026-10-11T04:13:37.835Z  

```py
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return False

        cnt = 0

        while n & 1 == 0:
            cnt += 1
            n = n >> 1
        
        if n == 1 and cnt % 2 == 0:
            return True
        return False
```

---

[View on LeetCode](https://leetcode.com/problems/power-of-four/)