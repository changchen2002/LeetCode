class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
    # 暴力思路：
    # 枚举删除所有括号的所有组合（DFS/BFS），找出能组成有效括号的字符串。
    # 每次删除一个字符直到出现有效结果。
        lrem=rrem=0
        for c in s:
            if c=='(':
                lrem+=1
            elif c==')':
                if lrem>0:
                    lrem-=1
                else:
                    rrem+=1
        
        res=set()
        def dfs(i,left,right,lrem,rrem,path):
            if i==len(s):
                if lrem==0 and rrem==0:
                    res.add(''.join(path))
                return
            c=s[i]
            if c=='(':
                if lrem>0:
                    dfs(i+1,left,right,lrem-1,rrem,path)
                dfs(i+1,left+1,right,lrem,rrem,path+[c])
            elif c==')':
                if rrem>0:
                    dfs(i+1,left,right,lrem,rrem-1,path)
                if left>right:
                    dfs(i+1,left,right+1,lrem,rrem,path+[c])            
                # 在回溯中，如果不手动回退（pop()），就必须用 path + [c]；
                # 如果显式回退，就能用 path.append(c) / path.pop()。
            else:
                dfs(i+1,left,right,lrem,rrem,path+[c])
        dfs(0,0,0,lrem,rrem,[])
        return list(res)