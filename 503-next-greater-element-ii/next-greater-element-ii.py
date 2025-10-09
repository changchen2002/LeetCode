class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dec=[]
        res=[-1]*n
        for i in range(2*n):
            while dec and nums[i%n]>nums[dec[-1]]:
                res[dec.pop()]=nums[i%n]
            dec.append(i%n)
        return res


        # dec     i       num    res
        # [0]     0        1      [-1,-1,-1]
        # [1]      1        2     [1,-1,-1]    
        # [1,2]    2        1      [2,-1,-1]
        # [1,2,1]   3        1     [2,-1,-1]
        # [1,2,]     4          2