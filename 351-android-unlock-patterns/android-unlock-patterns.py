class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        jump = {
            (1,3):2, (3,1):2,
            (1,7):4, (7,1):4,
            (3,9):6, (9,3):6,
            (7,9):8, (9,7):8,
            (1,9):5, (9,1):5,
            (3,7):5, (7,3):5,
            (2,8):5, (8,2):5,
            (4,6):5, (6,4):5
        }
        res=0
        vis=set()
        def dfs(last,length):
            nonlocal res
            if length>n:
                return
            if m<=length<=n:
                res+=1

            for i in range(1,10):
                if i not in vis:
                    if (last,i) not in jump or jump[(last,i)] in vis:
                        vis.add(i)
                        dfs(i,length+1)
                        vis.remove(i)
        
        for i in range(1,10):
            vis.add(i)
            dfs(i,1)
            vis.remove(i)
        return res
                    