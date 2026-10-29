class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[-1]*len(nums1)
        stack=[]
        dic={n:-1 for n in nums2}
        for n in nums2:
            while stack and stack[-1]<n:
                dic[stack.pop()]=n
            stack.append(n)
        
        for i,n in enumerate(nums1):
            ans[i]=dic[n]
        return ans