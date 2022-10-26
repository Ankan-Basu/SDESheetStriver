#https://leetcode.com/problems/two-sum/submissions/

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

#Optimal. Hash Map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        indx1 = indx2 = 0
        
        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in hashMap:
                indx1 = i
                indx2 = hashMap[needed]
                break
            else:
                hashMap[nums[i]] = i
                
        return [indx1, indx2]
      
     
#Brute Force    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
