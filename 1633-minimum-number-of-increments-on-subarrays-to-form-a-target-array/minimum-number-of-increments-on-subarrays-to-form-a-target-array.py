class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
        stack=[min(target)]
        res=min(target)
        for n in target:
            while stack[-1]>n:
                top=stack.pop()
                res+=top-max(stack[-1],n)
            stack.append(n)
        
        for i in range(1,len(stack)):
            res+=stack[i]-stack[i-1]
        return res

# stack   n    res
# [1,1]    1     1
# [1,1,2]   2     1
# [1,1,2,3] 3     1
# [1,1,2]   2     2
# [1,1,1]  1     3


