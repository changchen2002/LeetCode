class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        n=len(nums)
        bucket={i:[] for i in range(n+1)}
        for num,freq in count.items():
            bucket[freq].append(num)
        
        res=[]
        for i in range(n,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res