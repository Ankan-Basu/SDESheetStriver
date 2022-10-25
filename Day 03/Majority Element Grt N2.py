#https://leetcode.com/problems/majority-element/solution/

"""
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

#Sort and find center or
#Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        elem = 0
        
        for num in nums:
            if (count == 0):
                # count += 1
                elem = num
                
            if (num == elem):
                count += 1
            else:
                count -= 1
                
        return elem
