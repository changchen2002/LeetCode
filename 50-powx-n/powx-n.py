class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n==0:
                return 1
            if n<0:
                return 1.0/pow(x,-n)
            if n%2==1:
                return x*pow(x*x,(n-1)//2)
            else:
                return pow(x*x,n//2)
        return pow(x,n)