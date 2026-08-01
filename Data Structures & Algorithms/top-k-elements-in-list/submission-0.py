class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1
        
        result = sorted(dicts.items(), key=lambda x: x[1],reverse=True)
        result2 = result[:k]
        output = []
        for group in result2:
            output.append(group[0])
        return output
            
        