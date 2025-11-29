class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def divideConquer(a):
            nonlocal res
            if len(a)<=1:
                return a
            m=(len(a))//2
            left=divideConquer(a[:m])
            right=divideConquer(a[m:])

            merged=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]>2*right[j]:
                    res+=len(left)-i
                    j+=1
                else:
                    i+=1
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        res=0
        divideConquer(nums)
        return res