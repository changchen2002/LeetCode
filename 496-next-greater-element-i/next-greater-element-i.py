class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dec=[]
        hashmap={}
        for n in nums2:
            while dec and n>dec[-1]:
                top=dec.pop()
                hashmap[top]=n
            dec.append(n)
        
        for n in dec:
            hashmap[n]=-1
            
        return [hashmap[n] for n in nums1]