class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=['' for _ in range(numRows)]
        i,j,idx=0,0,0
        while idx<len(s):
            while i<numRows: 
                res[i]+=s[idx]
                idx+=1
                if idx==len(s):
                    break
                i+=1 
            i=numRows-1
            if idx==len(s):
                break
            while i>1:
                i-=1
                print(i)
                res[i]+=s[idx]
                idx+=1
                if idx==len(s):
                    break
            i=0
        return ''.join(res)