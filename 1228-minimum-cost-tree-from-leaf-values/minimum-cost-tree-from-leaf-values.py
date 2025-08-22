class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack=[float('inf')]
        res=0
        for n in arr:
            while stack[-1]<=n:
                mid=stack.pop()
                res+=mid*min(stack[-1],n)
            stack.append(n)
        while len(stack)>2:
            res+=stack.pop()*stack[-1]
        return res
