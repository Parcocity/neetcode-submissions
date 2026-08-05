class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            max_length = 0
            j = i
            while (j >= 0):
                if nums[j] < nums[i]:
                    max_length = max(dp[j], max_length)
                j -= 1
            dp[i] = max_length + 1
        return max(dp)
                




        