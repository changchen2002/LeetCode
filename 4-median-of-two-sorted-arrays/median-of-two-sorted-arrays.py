class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        half=(m+n+1)//2
        l,r=0,m

        while True:
            i=l+(r-l)//2
            j=half-i

            Aleft=nums1[i-1] if i>0 else float('-inf')
            Aright=nums1[i] if i<m else float('inf')
            Bleft=nums2[j-1] if j>0 else float('-inf')
            Bright=nums2[j] if j<n else float('inf')
            
            if Aleft<=Bright and Bleft<=Aright:
                if (m+n)%2:
                    return max(Aleft,Bleft)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1

