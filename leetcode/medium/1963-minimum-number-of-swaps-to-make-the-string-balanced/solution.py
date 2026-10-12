class Solution:
    def minSwaps(self, s: str) -> int:
        
        mx_cnt = 0
        cnt = 0
        for x in s:

            if x == "[":
                cnt -= 1
            else:
                cnt += 1
            
            mx_cnt = max(mx_cnt,cnt)
            
        return (mx_cnt + 1) // 2