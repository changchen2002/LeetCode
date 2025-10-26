class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(st):
            l=0
            for c in st:
                if c=='(':
                    l+=1
                elif c==')':
                    l-=1
                    if l<0:
                        return False
            return l==0
        
        seen={s}
        res=[]
        q=deque([s])
        found=False
        while q:
            cur=q.popleft()
            if isValid(cur):
                res.append(cur)
                found=True
            if found:
                continue
            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue
                nxt=cur[:i]+cur[i+1:]
                if nxt not in seen: #这里剪枝才是对的
                    seen.add(nxt)
                    q.append(nxt)
        return res