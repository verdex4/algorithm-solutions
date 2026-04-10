from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        # lists of seen sets
        rows_seen = [set() for _ in range(n)]
        cols_seen = [set() for _ in range(n)]
        squares_seen = [set() for _ in range(n)]

        def square_idx(i, j):
            return (i // 3) * 3 + (j // 3)

        for i in range(n):
            for j in range(n):
                value = board[i][j]
                if value == '.':
                    continue
                if (value in rows_seen[i] 
                    or value in cols_seen[j] 
                    or value in squares_seen[square_idx(i, j)]):
                    return False
                rows_seen[i].add(value)
                cols_seen[j].add(value)
                squares_seen[square_idx(i, j)].add(value)
        
        return True

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))