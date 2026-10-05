# Jewels and Stones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

 

 **Example 1:** 

```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

```

 **Example 2:** 

```
Input: jewels = "z", stones = "ZZ"
Output: 0

```

 

 **Constraints:** 

- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters.
- All the characters of jewels are unique.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 2.30%)  
**Memory:** 19.3 MB (beats 55.79%)  
**Submitted:** 2026-10-05T11:31:56.612Z  

```py
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        i = 0
        sm = 0
        while i < len(jewels):
            j = 0
            while j < len(stones):
                if jewels[i] == stones[j]:
                    sm += 1
                j += 1
            i += 1
        return sm
```

---

[View on LeetCode](https://leetcode.com/problems/jewels-and-stones/)