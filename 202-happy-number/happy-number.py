class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def get_next(n):
            total=0
            while n>0:
                total+=(n%10)**2
                n=n//10
            return total
        while n!=1 and n not in seen:
            seen.add(n)
            n=get_next(n)
        return n==1
            
            