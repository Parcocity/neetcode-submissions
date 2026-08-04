from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        right_max = [0]*n
        right_max[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j])

        res = 0
        for ptr in range(1, n):
            vol = min(left_max[ptr], right_max[ptr]) - height[ptr]
            if vol < 0:
                vol = 0
            res += vol
        return res
