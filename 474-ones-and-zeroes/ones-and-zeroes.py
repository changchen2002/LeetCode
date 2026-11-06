class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        @cache
        def dfs(i,j,idx):
            if idx==len(strs):
                return 0
            
            add=0
            z=strs[idx].count("0")
            o=strs[idx].count("1")

            if i+z<=m and j+o<=n:
                add=1+dfs(i+z,j+o,idx+1)

            skip=dfs(i,j,idx+1)
            
            return max(add,skip)

        return dfs(0,0,0)