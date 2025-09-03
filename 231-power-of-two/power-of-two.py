class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False

        while n>1:
            n,mod=divmod(n,2)
            if mod!=0:
                return False
        return True
    