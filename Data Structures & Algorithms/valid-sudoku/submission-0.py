class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows = set()
            cols = set()
            for j in range(9):
                if board[i][j] in rows or board[j][i] in cols:
                    return False
                if board[i][j] != '.':
                    rows.add(board[i][j])
                if board[j][i] != '.':
                    cols.add(board[j][i])
        
        for grid in range(9):
            r, c = (grid // 3) * 3, (grid%3) * 3
            seen = set()
            for dr in range(3):
                for dc in range(3):
                    val = board[r+dr][c+dc]
                    if val in seen and val != '.':
                        return False
                    seen.add(board[r+dr][c+dc])
                    
        return True