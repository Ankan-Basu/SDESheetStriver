#https://leetcode.com/problems/merge-intervals/submissions/

"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

class Solution:
    def isMergeble(self, intv1, intv2):
        return (intv1[-1] >= intv2[0])
    
    def mergeIntv(self, intv1, intv2):
        intv = [None] * 2
        intv[0] = intv1[0]
        nextVal = intv1[-1] if (intv1[-1] > intv2[-1]) else intv2[-1]
        intv[-1] = nextVal
        return intv
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
    
        tmp = intervals[0]
        for i in intervals[1::]:
            if (self.isMergeble(tmp, i)):
                tmp = self.mergeIntv(tmp, i)
            else:
                res.append(tmp)
                tmp = i
                
        res.append(tmp)     
        return res
