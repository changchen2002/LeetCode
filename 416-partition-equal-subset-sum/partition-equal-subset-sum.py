class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target= sum(nums)/2
        dp=set()
        dp.add(0)
        for i in range(len(nums)):
            temp=set()
            for j in dp:
                temp.add(nums[i]+j)
                temp.add(j)
            if target in temp:
                return True
            dp=temp
        return False
            
