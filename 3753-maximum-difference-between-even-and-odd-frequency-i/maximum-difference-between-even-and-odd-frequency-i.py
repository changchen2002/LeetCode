class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        print(count)
        maxOdd=0
        minEven=float('inf')
        for freq in count.values():
            print(freq)
            if freq%2:
                maxOdd=max(maxOdd,freq)
            else:
                minEven=min(minEven,freq)
        return maxOdd-minEven if minEven!=float('inf') else maxOdd