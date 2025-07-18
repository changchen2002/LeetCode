class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub=[set() for _ in range(9)]
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                if val in rows[r] or val in cols[c] or val in sub[(r//3)*3+c//3]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                sub[(r//3)*3+c//3].add(val)
        return True

            
