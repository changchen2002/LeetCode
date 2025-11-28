class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        count=Counter(a%space for a in nums)
        mxm=max(count.values())
        return min(a for a in nums if count[a%space]==mxm)