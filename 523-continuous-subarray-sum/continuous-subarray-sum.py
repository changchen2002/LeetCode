class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap={0:-1}
        cur=0
        for i,n in enumerate(nums):
            cur+=n
            target=cur%k
            if target in hashmap.keys():
                if i-hashmap[target]>=2:
                    return True
            else:
                hashmap[target]=i
        return False

        # sum(subarray) % k == 0
        # (pre[j] - pre[i]) % k == 0
        # pre[j] % k == pre[i] % k