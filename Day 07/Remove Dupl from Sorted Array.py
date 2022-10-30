#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = ptr2 = 0
        
        while(ptr2 < len(nums)):
            if (nums[ptr2] == nums[ptr1]):
                ptr2 += 1
            else:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]
        
        
        return ptr1 + 1 #since it is 0 based index
