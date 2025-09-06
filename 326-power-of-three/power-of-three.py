class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        
        while True:
            div,mod=divmod(n,3)
            if div==0 and mod==1:
                return True
            if mod!=0:
                return False
            n=div
