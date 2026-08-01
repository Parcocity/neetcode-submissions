class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(0, len(nums)-1):
            prefix.append(prefix[i] * nums[i])
            suffix.append(suffix[i] * nums[len(nums) - 1 - i])
        
        return list(prefix[j] * suffix[len(nums)- 1- j] for j in range(0, len(nums)))



        