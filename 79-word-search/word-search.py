class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        visited=set()
        def dfs(r,c,i):
            if i==len(word):
                return True

            for dr,dc in directions:
                if ((r+dr) in range(rows) and
                    (c+dc) in range(cols) and
                    board[r+dr][c+dc]==word[i] and
                    (r+dr,c+dc) not in visited):
                    visited.add((r+dr,c+dc))
                    if dfs(r+dr,c+dc,i+1):
                        return True
                    visited.remove((r+dr,c+dc))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    visited.add((r,c))
                    if dfs(r,c,1):
                        return True
                    visited.remove((r,c))    
        return False

