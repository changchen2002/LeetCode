class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #左->右. i不确定<k<j确定
        #左<-右. i<k确定<j确定

        dec=[]
        m=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<m<dec[0]:
                return True
            while dec and nums[i]>dec[-1]:
                m=max(m,dec.pop())
            dec.append(nums[i])
        return False