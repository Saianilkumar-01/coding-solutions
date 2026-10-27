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
**Runtime:** 8744 ms (beats 5.01%)  
**Memory:** 19.2 MB (beats 88.69%)  
**Submitted:** 2026-10-27T04:33:08.408Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        for i in range(len(s)):
            for j in range(i,len(s)):
                ch = s[i:j+1]
                if ch == ch[::-1]:
                    if len(res) < len(ch):
                        res = ch

        return res
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)