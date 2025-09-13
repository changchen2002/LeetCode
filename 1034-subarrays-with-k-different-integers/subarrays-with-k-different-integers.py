class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #滑动窗口不是直接数所有子数组，而是通过维护窗口内的性质
        def atMostK(k):
            count=defaultdict(int)
            l=total=0
            for r in range(len(nums)):
                count[nums[r]]+=1
                while len(count)>k:
                    count[nums[l]]-=1
                    if count[nums[l]]==0:
                        del count[nums[l]]
                    l+=1
                total+=r-l+1
            return total

        return atMostK(k)-atMostK(k-1)