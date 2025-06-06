class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #堆查找时间O(n)
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        bucket=[[]for i in range(len(nums)+1)] #index+1
        for num,freq in hashmap.items():
            bucket[freq].append(num) #maxFreqIndex=len(nums)

        res=[]
        for freq in range(len(bucket)-1,0,-1): #遍历到0因为bucket里频率最小为0
            for num in bucket[freq]:
                res.append(num)
                if len(res)==k:
                    return res
