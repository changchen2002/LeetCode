class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==0:
            return []
        if n==1:
            return [0]
        if n==2:
            return [-1,1]
        res=[]
        for i in range(1,n//2+1):
            res.append(-i) 
            res.append(i)
        if len(res)<n:
            res.append(0)
        return res

