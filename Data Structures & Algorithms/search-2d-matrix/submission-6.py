class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left1 = 0
        right1 = m - 1
        row = -1
        while(left1 <= right1):
            mid = (left1 + right1) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                right1 = mid - 1
            else:
                left1 = mid + 1
        if row == -1:
            return False
        
        
        left2 = 0
        right2 = n - 1
        while(left2 <= right2):
            mid = (left2 + right2) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        return False
            
            




        