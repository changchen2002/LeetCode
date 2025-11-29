class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s=[0]
        for x in nums:
            s.append(s[-1]+x)
        def sort(a):
            n=len(a)
            if n<=1:
                return a
            m=n//2
            left=sort(a[:m])
            right=sort(a[m:])

            i=j=k=0
            nonlocal res
            for x in right:
                lo=x-upper
                hi=x-lower
                while i<len(left) and left[i]<lo:i+=1
                while j<len(left) and left[j]<=hi:j+=1
                res+=j-i
            merged=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    merged.append(left[i]);i+=1
                else:
                    merged.append(right[j]);j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        
        res=0
        sort(s)
        return res