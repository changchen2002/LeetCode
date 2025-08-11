class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[] for i in range(len(nums)+1)]
        count=Counter(nums)
        for num,freq in count.items():
            bucket[freq].append(num)
        res=[]
        for i in range(len(bucket)-1,-1,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
