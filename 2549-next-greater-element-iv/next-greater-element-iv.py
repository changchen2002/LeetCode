class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        s1,s2=[],[]

        for i,x in enumerate(nums):
            while s2 and x>nums[s2[-1]]:
                res[s2.pop()]=x
            temp=[]
            while s1 and x>nums[s1[-1]]:
                temp.append(s1.pop())
            while temp:
                s2.append(temp.pop())
            s1.append(i)
        return res


