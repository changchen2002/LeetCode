class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res,stack=[0]*len(temperatures),[0]
        for i,num in enumerate(temperatures):
            while stack and num>temperatures[stack[-1]]:
                res[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return res
