# Longest Palindromic Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, return  *the longest*   *palindromic*   *substring*  in `s`.

 

 **Example 1:** 

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

```

 **Example 2:** 

```
Input: s = "cbbd"
Output: "bb"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solution

**Language:** Python  
**Runtime:** 232 ms (beats 82.26%)  
**Memory:** 19.2 MB (beats 66.58%)  
**Submitted:** 2026-10-27T04:52:59.547Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_length = 1
        start = 0

        for i in range(len(s)):
            p1 = i
            p2 = i

            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            length = p2 - p1 - 1
            if length > max_length:
                max_length =  length
                start = p1 + 1
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            length = p2 - p1 -1
            if max_length < length:
                max_length = length
                start = p1 + 1
        return s[start:start+max_length]
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)