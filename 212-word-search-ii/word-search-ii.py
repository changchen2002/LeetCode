class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n=len(board),len(board[0])
        trie={}
        for w in words:
            cur=trie
            for c in w:
                if c not in cur: cur[c]={}
                cur=cur[c]
            cur['#']=w

        res=set()
        def dfs(i,j,node):
            if '#' in node:
                res.add(node['#'])
                del node['#']
            if i<0 or i>=m or j<0 or j>=n or board[i][j] not in node:
                return
            c=board[i][j]
            board[i][j]='#'
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i+x,j+y,node[c])
            board[i][j]=c

        for i in range(m):
            for j in range(n):
                dfs(i,j,trie)
        return list(res)
