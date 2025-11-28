class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr)<2:
            return 0
        l,r=0,len(arr)-1
        while l<r:
            m=l+(r-l)//2
            if arr[m]<arr[m+1]:
                l=m+1
            elif arr[m]>arr[m+1]:
                r=m
        return l