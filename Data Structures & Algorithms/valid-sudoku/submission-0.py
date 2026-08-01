class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                seen.add(board[i][j])
                
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for m in range(3):
            for n in range(3):
                row = m * 3
                col = n * 3
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] == ".":
                            continue
                        elif board[row + i][col + j] in seen:
                            return False
                        seen.add(board[row + i][col + j])
                        
        return True


                


