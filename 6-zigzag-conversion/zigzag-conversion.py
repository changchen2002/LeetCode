class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=['' for _ in range(numRows)]
        r=0
        down=False
        for c in s:
            rows[r]+=c
            if r==0 or r==numRows-1:
                down=not down
            r+=1 if down else -1
        return ''.join(rows)