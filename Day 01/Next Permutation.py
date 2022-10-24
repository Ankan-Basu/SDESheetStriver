#https://leetcode.com/problems/next-permutation/

"""
Input: nums = [1,2,3]
Output: [1,3,2]
  
Input: nums = [3,2,1]
Output: [1,2,3]
"""


class Solution:
    def reverse(self, nums, start, end):
        i = start
        j = end
        while(i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def nextPermutation(self, nums: List[int]) -> None:
        size = len(nums)
        prev = nums[-1]
        indx = -1
        for i in range(size-2, -1, -1):
            curr = nums[i]
            if (curr < prev):
                indx = i
                break
            prev = curr
                
        if (indx >= 0):
            for i in range(size-1, indx, -1):
                if (nums[i] > nums[indx]):
                    nums[i], nums[indx] = nums[indx], nums[i]
                    break
                    
            
            self.reverse(nums, indx+1, size-1)
        else:
            nums.reverse()
