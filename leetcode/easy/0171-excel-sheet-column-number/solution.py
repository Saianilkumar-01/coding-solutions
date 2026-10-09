class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        sm = 0
        for x in columnTitle:
            sm = sm * 26 + (ord(x)-ord('A')+1)
        
        return sm