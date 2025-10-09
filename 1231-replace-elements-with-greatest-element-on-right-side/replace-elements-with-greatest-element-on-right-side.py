class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        inc=[]

        for i in range(len(arr)-1,-1,-1):
            n=arr[i]
            arr[i]=inc[-1] if inc else -1
            if not inc or n>inc[-1]:
                inc.append(n)
        
        return arr