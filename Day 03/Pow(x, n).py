#https://leetcode.com/problems/powx-n/


"""
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


"""
x^n = (x*x)^(n/2) if n is even
x = x * (x)^(n-1) if n is odd
  = x * (x*x)((n-1)/2)
use this for recur. O(logn) better than simply multiplying linearly

for n negative
x^(-n) = 1/(x^n)
ie 1/f(x, -n)

Beware
-2^31 <= n <= (2^31)-1
if n is -2^31, making it positive will cause overflow in some lang, so convert to long
"""

class Solution:
    def f(self, x, n):
        if (n==0):
            return 1
        
        if (n%2 == 0):
            return self.f(x*x, n/2)
        else:
            return x*self.f(x*x, (n-1)/2)
        
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if (n < 0):
            return 1/self.f(x, -n)
        else:
            return self.f(x,n)
