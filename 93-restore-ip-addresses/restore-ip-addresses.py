class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def backtrack(i,path):
            if len(path)==4:
                if i==len(s):
                    res.append('.'.join(path))
                return
            
            for end in range(i+1,min(i+4,len(s)+1)):
                part=s[i:end]
                if part.startswith('0') and len(part)>1 or int(part)>255:
                    continue
                backtrack(end,path+[part])
        backtrack(0,[])
        return res