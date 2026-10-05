class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend = set(friends)
        res = []

        for x in order:
            if x in friend:
                res.append(x)
        return res