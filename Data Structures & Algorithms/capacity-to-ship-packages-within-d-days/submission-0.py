class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while (left < right):
            mid = (left + right) // 2
            day = 1
            total = 0
            
            for weight in weights:
                if (weight + total > mid):
                    day += 1
                    total = weight
                else:
                    total += weight
            
            if day > days:
                left = mid + 1
            else:
                right = mid 
        return left
