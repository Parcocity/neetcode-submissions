import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hashmap = {}
        for i in range(len(points)):
            dis = math.sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(heap, -dis)
            hashmap[i] = -dis
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(len(points)):
            if hashmap[i] in heap:
                res.append(points[i])
        return res
        