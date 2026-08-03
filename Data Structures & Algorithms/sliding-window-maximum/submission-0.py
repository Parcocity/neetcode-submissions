from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for ptr, num in enumerate(nums):
            while(len(dq) > 0 and num > nums[dq[-1]]):
                dq.pop()
            dq.append(ptr)
            if ptr >= k - 1:
                res.append(nums[dq[0]])
                if (ptr - k + 1) in dq:
                    dq.remove(ptr - k + 1)
        return res







        