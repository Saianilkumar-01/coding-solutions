class Solution:
    def checkString(self, s: str) -> bool:
        found = False
        for i in range(len(s)):

            if s[i] == 'b':
                found = True
            elif s[i] == 'a' and found == True:
                return False
        return True