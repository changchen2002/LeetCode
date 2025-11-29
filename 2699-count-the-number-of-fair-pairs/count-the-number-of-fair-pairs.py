class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def count(target):
            l = 0 
            r = len(nums) - 1
            res = 0

            while l < r:
                total = nums[l] + nums[r]
                if total <= target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            return res
        
        return count(upper) - count(lower - 1)
        