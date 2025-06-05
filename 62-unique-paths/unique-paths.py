class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions=[[0,1],[1,0]]
        memo={}
        def dfs(r,c):
            if r==m-1 and c==n-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            count=0
            for dr,dc in directions:
                if (r+dr in range(m) and
                    c+dc in range(n)):
                    count+=dfs(r+dr,c+dc)
            memo[(r,c)]=count
            return count
        return dfs(0,0)


