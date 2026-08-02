class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        minimal = len(nums)
        left = 0
        sums = 0
        for right, num in enumerate(nums):
            sums += num
            while (sums >= target):
                minimal = min(minimal, right - left + 1)
                sums -= nums[left]
                left += 1
        return minimal
            
                

