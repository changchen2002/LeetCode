class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree={}
        for x in nums:
            a,b,c=x//100,(x//10)%10,x%10
            tree[(a,b)]=c

        def dfs(d,p,path):
            if (d,p) not in tree:
                return 0
            path+=tree[(d,p)]
            l,r=(d+1,p*2-1),((d+1,p*2))
            if l not in tree and r not in tree:
                return path
            return dfs(d+1,p*2-1,path)+dfs(d+1,p*2,path)
        return dfs(1,1,0)

