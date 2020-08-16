class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        close=float('-inf')
        count=0
        
        for interval in sorted(intervals, key=lambda x: x[1]):
            if interval[0]>=close:
                close=interval[1]
            else:
                count+=1
        return count