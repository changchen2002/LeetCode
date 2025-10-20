class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        bucket=[[] for _ in range(len(s)+1)] 
        for c,freq in count.items():
            bucket[freq].append(c) 

        res=[]
        for i in range(len(bucket)-1,-1,-1):
            for c in bucket[i]:
                res.append(c*i)
        return "".join(res)