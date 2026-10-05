class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        i = 0
        j = 0
        res = []
        while i < len(order):
            j = 0
            while j < len(friends):
                if order[i] == friends[j]:
                    res.append(order[i])
                j += 1
            i += 1
        return res