class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seem={}
        for i,num in enumerate(nums):
            if num in seem and i-seem[num]<=k:
                return True
            seem[num]=i
        return False
