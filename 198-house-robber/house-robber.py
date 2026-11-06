class Solution:
    def rob(self, nums: list[int]) -> int:
        m=[0]*(len(nums)+1)
        m[1]=nums[0]

        for i in range(1,len(nums)):
            m[i+1]=max(m[i],m[i-1]+nums[i])
        
        return m[-1]
