#https://leetcode.com/problems/linked-list-cycle/

#First step of Floyd's Cycle Detection Algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastPtr = slowPtr = head
        
        if (head ==  None):
            return False
        
        found = False
        while (fastPtr and fastPtr.next):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            if (slowPtr == fastPtr):
                found = True
                break
                
        return found
