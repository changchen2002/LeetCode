class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        dic={n:-1 for n in nums2}
        for n in nums2:
            while stack and stack[-1]<n:
                dic[stack.pop()]=n
            stack.append(n)
        
        return [dic[n] for n in nums1]