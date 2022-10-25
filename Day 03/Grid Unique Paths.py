#https://leetcode.com/problems/unique-paths/

"""
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

class Solution:
    def nCr (self, n, r):
        numerator = denominator = 1
        for i in range(n, (n-r+1)-1, -1):
            numerator *= i
            
        for i in range(r, 1, -1):
            denominator *= i
        
        # print(numerator, denominator)
        res = int(numerator/denominator)
        return res
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.nCr(m+n-2, m-1)    
