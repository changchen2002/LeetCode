class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        while True:
            n-=i+1
            if n<0:
                return i
            elif n==0:
                return i+1
            i+=1