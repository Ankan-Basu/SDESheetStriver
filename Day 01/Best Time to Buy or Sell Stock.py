#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - currMin
            maxProfit = max(maxProfit, profit)
            currMin = min(currMin, prices[i])
            
        return maxProfit
