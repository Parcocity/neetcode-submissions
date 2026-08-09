class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = -1
        left = 1
        right = max(piles)
        while (left <= right):
            mid = (left + right) // 2
            hour = 0
            for pile in piles:
                if pile % mid  == 0:
                    hour += pile // mid
                else:
                    hour += pile // mid + 1
            if hour > h:
                left = mid + 1
            else:
                min_rate = mid
                right = mid - 1
        return min_rate


        