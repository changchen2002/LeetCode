class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def helper(i,target):
            indexs=[]
            l,r=i,len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    indexs.append([nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l]+nums[r]>target:
                        r-=1
                else:
                        l+=1
            return indexs

        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            threeSum=target-nums[i]
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                indexs=helper(j+1,threeSum-nums[j])
                for index in indexs:
                    res.append([nums[i], nums[j]] + index)
        return res