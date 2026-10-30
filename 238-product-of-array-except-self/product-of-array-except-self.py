class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans=[1]*len(nums)
        front=[1]*len(nums)
        back=[1]*len(nums)
        p=1
        for i,n in enumerate(nums):
            p*=n
            # print(p)
            front[i]=p
            # print(front)
        p=1
        for i in range(len(nums)-1,-1,-1):
            p*=nums[i]
            # print(p)
            back[i]=p
            # print(back)
        # print(front,back)
        for i in range(len(ans)):
            if i==0:
                ans[i]=back[i+1]
            elif i==len(ans)-1:
                ans[i]=front[i-1]
            else:
                ans[i]=front[i-1]*back[i+1]
        
        return ans

        
# i, n, p,  front
# 0, 1, 1     1
# 1, 2, 2     1,2

