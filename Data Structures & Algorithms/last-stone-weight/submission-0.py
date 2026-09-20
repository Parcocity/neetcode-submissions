import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        
        while (len(heap) >= 2):
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            if num1 == num2:
                continue
            else:
                heapq.heappush(heap, num1 - num2)
        
        if len(heap) == 0:
            return 0
        else:
            return heap[0]* (-1)
        