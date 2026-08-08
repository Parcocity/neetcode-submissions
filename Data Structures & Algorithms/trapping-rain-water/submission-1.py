from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        prefix = [0] * n
        prefix[0] = height[0]
        suffix = [0] * n
        suffix[-1] = height[-1]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])
        for j in range(n-2, -1, -1):
            suffix[j] = max(suffix[j+1], height[j])
        
        for k in range(n):
            vol = min(prefix[k],suffix[k]) - height[k]
            if vol < 0:
                continue
            else:
                res += vol
        
        return res




        
