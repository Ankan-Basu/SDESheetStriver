#https://leetcode.com/problems/pascals-triangle/

"""
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        prev = [1]
        for i in range(1, numRows):
            curr = [1]*(len(prev) + 1)
            for j in range(len(curr)):
                if (j != 0 and j!= len(curr)-1):
                    # print(j)
                    # print(len(curr)-1)
                    curr[j] = prev[j-1] + prev[j]
                    
            res.append(curr)
            prev = curr.copy()
            
        
        return res
