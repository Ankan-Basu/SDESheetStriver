#https://leetcode.com/problems/majority-element-ii/

"""
Input: nums = [3,2,3]
Output: [3]

Input: nums = [1]
Output: [1]

Input: nums = [1,2]
Output: [1,2]
"""

#Modified Voter's Algo

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        
        target = len(nums)//3
        
        count1 = count2 = 0
        num1 = num2 = 0
        
        for i in nums:
            #why this works?
            if (num1 == i):
                count1 += 1
            elif (num2 == i):
                count2 += 1
            ##
            #why not this at beginning of "if" possible?
            elif (count1 == 0):
                num1 = i
                count1 = 1
            elif (count2 == 0):
                num2 = i
                count2 = 1
            # elif (num1 == i):
            #     count1 += 1
            # elif (num2 == i):
            #     count2 += 1
            else:
                count1 -= 1
                count2 -= 2
                
        count1_verify = count2_verify = 0
        
        print (num1, num2)
        for i in nums:
            if (num1 == i):
                count1_verify += 1
            elif (num2 == i):
                count2_verify += 1
                
        if (count1_verify > target):
            res.append(num1)
        if (count2_verify > target):
            res.append(num2)
        
        return res
        
