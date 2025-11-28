class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        arr=list(enumerate(nums))

        def mergeSort(a):
            if len(a)<=1:
                return a
            mid=len(a)//2
            left=mergeSort(a[:mid])
            right=mergeSort(a[mid:])

            i=j=0
            merged=[]
            while i<len(left) and j<len(right):
                # print(left,right,res)
                if left[i][1]>right[j][1]:
                    res[left[i][0]]+=len(right)-j
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            merged.extend(left[i:])
            merged.extend(right[j:])
            # print(merged,res)
            return merged
        
        mergeSort(arr)
        return res