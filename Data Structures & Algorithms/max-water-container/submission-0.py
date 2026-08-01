class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        area = (end - start) * min(heights[start], heights[end])

        while (start < end):
            if (heights[start] <= heights[end]):
                start += 1
            else:
                end -= 1
            new_area = (end - start) * min(heights[start], heights[end])
            if new_area > area:
                area = new_area
        
        return area
            
