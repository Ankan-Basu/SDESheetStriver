#https://leetcode.com/problems/find-the-duplicate-number/

"""
Input: nums = [3,1,3,4,2]
Output: 3
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = tort = 0
        
        while(True):
            tort = nums[tort]
            hare = nums[nums[hare]]
            if (hare == tort):
                break
                
        hare = 0
        while(hare != tort):
            tort = nums[tort]
            hare = nums[hare]
            
        return tort
