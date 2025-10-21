class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<2:
            return True
        intervals.sort()
        pre=intervals[0][1]
        for s,e in intervals[1:]:
            if pre>s:
                return False
            pre=e
        return True