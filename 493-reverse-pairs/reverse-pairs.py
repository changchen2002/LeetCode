class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res=0
        a=list(enumerate(nums))
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
                if left[i][1]>2*right[j][1]:
                    res+=len(right)-j
                    i+=1
                else:
                    j+=1
            i=j=0
            while i<len(left) and j<len(right):
                if left[i][1]>right[j][1]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        divideConquer(a)
        return res