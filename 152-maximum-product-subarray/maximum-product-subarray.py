class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum=minNum=res=nums[0]
        
        for num in nums[1:]: 
            if num<0:
                maxNum,minNum=minNum,maxNum
            maxNum=max(num,maxNum*num)
            minNum=min(num,minNum*num)
            res=max(res,maxNum) 

        return res
