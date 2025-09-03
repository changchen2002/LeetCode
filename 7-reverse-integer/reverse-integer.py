class Solution:
    def reverse(self, x: int) -> int:
        sign=1 if x>0 else -1
        rev,x=0,abs(x)
        while x:
            x,mod=divmod(x,10)
            if rev>(2**31-1)//10:
                return 0
            elif rev==(2**31-1)//10 and mod>7:
                return 0
            rev=rev*10+mod
        return sign*rev