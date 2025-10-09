class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        dec=[]
        for i,t in enumerate(temperatures):
            while dec and temperatures[dec[-1]]<t:
                idx=dec.pop()
                res[idx]=i-idx
            dec.append(i)
        return res