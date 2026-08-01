class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = defaultdict()
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        max_length = 0
        while len(num_dict) > 0:
            result = []
            start = min(num_dict)
            while start in num_dict:
                result.append(start)
                num_dict.pop(start)
                start += 1
            if max_length < len(result):
                max_length = len(result)
        return max_length

        