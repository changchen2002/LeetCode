class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits="123456789"
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        subs=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                d=board[r][c]
                if d!=".":
                    rows[r].add(d)
                    cols[c].add(d)
                    box=(r//3)*3+(c//3) #背
                    subs[box].add(d)

        dirs=[(0,1),(0,-1),(-1,0),(1,0)]
        def dfs(pos):
            if pos==81:
                return True
            r,c=divmod(pos,9) #背
            if board[r][c]!='.':
                return dfs(pos+1) #填下一格
            box=(r//3)*3+(c//3)
            for d in digits:
                if d not in rows[r] and d not in cols[c] and d not in subs[box]:
                    rows[r].add(d)
                    cols[c].add(d)
                    subs[box].add(d)
                    board[r][c]=d
                    if dfs(pos+1):
                        return True #到底了, 结束所有递归
                    rows[r].remove(d)
                    cols[c].remove(d)
                    subs[box].remove(d)
                    board[r][c]='.'
            return False

        dfs(0)
        return board
    # 012
    # 345
    # 678

    # (0,8) - 2
    # (2,0)
    # (5,0) - 3
    # (8,0) - 6
    # (8,8) - 8
    # //3) + c//3