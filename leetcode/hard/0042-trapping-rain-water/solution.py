class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        lmax = [0]*len(height)
        rmax = [0]*len(height)

        lmax[0] = height[0]
        rmax[-1] = height[-1]

        for i in range(1,n):
            lmax[i] = max(lmax[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            rmax[i] = max(rmax[i+1] , height[i])

        sm = 0
        for i in range(n):
            sm += (min(lmax[i],rmax[i]) - height[i])

        return sm 