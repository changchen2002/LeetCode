class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            board[r][c]='.'
            i,j=1,1
            while r+i<rows and board[r+i][c]=='X':
                board[r+i][c]='.'
                i+=1
            while c+j<cols and board[r][c+j]=='X':
                board[r][c+j]='.'
                j+=1
                        
        res=0
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='X':
                    res+=1
                    dfs(r,c)
        return res