class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decq=deque()
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while decq and t>decq[-1][0]:
                tem,j=decq.pop()
                res[j]=i-j
            decq.append([t,i])
        return res