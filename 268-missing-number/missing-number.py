class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # index:  0 1 2 3
        # number: 3 0 1 (2: missing)

        res = len(nums) #add the missing index
        for i,n in enumerate(nums):
            res+=i-n
        return res