class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        sign=1
        i=0
        if s[0]=='-':
            sign=0
            i=1
        elif s[0]=='+':
            i=1
        res=0
        while i<len(s) and s[i].isdigit():
            if res>2**31//10 or (res==2**31//10 and int(s[i])>7):
                return 2**31-1 if sign else -2**31
            res=res*10+int(s[i])
            i+=1

        return res if sign else -res