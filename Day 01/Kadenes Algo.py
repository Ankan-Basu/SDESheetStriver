#https://leetcode.com/problems/maximum-subarray/

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = globalMax = nums[0]
        
        '''
        Kadene's Algo
        max sum subarr ending at index i = 
        max((max_sum_sub_arr_ending_at_indx(i - 1) + arr[i]), arr[i])
        '''
        for i in range(1, len(nums)):
            currMax = max(currMax+nums[i], nums[i])
            globalMax = max(globalMax, currMax)
            
        return globalMax
