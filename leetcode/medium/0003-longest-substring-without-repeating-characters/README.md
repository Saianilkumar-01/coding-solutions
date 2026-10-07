# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 187 ms (beats 80.90%)  
**Memory:** 20 MB (beats 37.05%)  
**Submitted:** 2026-10-07T16:55:37.155Z  

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        ans = 0

        for x in range(len(s)):

            if s[x] in hm:
                l = max(l,hm[s[x]]+1)

            hm[s[x]] = x
            ans = max(ans,x-l+1)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)