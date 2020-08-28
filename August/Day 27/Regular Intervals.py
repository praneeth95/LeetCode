import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals=sorted([[b,e,indx] for indx,[b,e] in enumerate(intervals)])
        res=[-1] * len(intervals)
        beginning_vals=[b for b,e,indx in intervals]
        
        for b,e,indx in intervals:
            x=bisect.bisect_left(beginning_vals,e)
            if x != len(beginning_vals):
                res[indx]=intervals[x][-1]
        return res