class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #36
        hashmap={}
        for i,n in enumerate(nums):
            if n in hashmap.keys():
                return [i,hashmap[n]]
            hashmap[target-n]=i