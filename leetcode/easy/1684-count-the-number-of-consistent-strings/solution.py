class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        list_str = list(allowed)
        cnt = 0
        for x in words:
            flag = True
            for j in range(len(x)):
                if x[j] not in list_str:
                    flag = False
                    break 
            if flag:
                cnt += 1
        
        return cnt