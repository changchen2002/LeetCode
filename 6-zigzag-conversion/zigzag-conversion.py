class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        res=['' for _ in range(numRows)]
        row=0
        up=False
        for c in s:
            res[row]+=c
            if row==0 or row==numRows-1:
                up=not up
            row+=1 if up else -1
        return ''.join(res)