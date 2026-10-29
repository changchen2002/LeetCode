class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]
        res=[-1]*len(nums)
        for i,n in enumerate(nums):
            while stack and n>nums[stack[-1]]:
                res[stack.pop()]=n
            stack.append(i)
        
        for i,n in enumerate(nums):
            while stack and n>nums[stack[-1]]:
                res[stack.pop()]=n
            stack.append(i)
        
        return res

# stack         res
# []          [-1,-1,-1]
# [0]         [-1,-1,-1]
# [1]         [2,-1,-1]
# [1,2]       [2,-1,-1]
# [1,2,0]     [2,-1,-1]
# [1,1]       [2,-1,2]
# [1,1,2]       