class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        res=['' for _ in range(numRows)]
        row=0
        down=False
        for c in s:
            res[row]+=c
            if row==0 or row==numRows-1:
                down=not down
            row+=1 if down else -1
        return ''.join(res)