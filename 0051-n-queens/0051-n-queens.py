class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                board = ["".join(row) for row in chessboard]
                solutions.append(board)
                return
            
            for col in range(n):
                if col in columns or (row - col) in left_diagonals or (row + col) in right_diagonals:
                    continue
                
                chessboard[row][col] = 'Q'
                columns.add(col)
                left_diagonals.add(row - col)
                right_diagonals.add(row + col)
                
                backtrack(row + 1)
                
                chessboard[row][col] = '.'
                columns.remove(col)
                left_diagonals.remove(row - col)
                right_diagonals.remove(row + col)
        
        solutions = []
        chessboard = [["." for _ in range(n)] for _ in range(n)]
        columns = set()
        left_diagonals = set()
        right_diagonals = set()
        
        backtrack(0)
        
        return solutions