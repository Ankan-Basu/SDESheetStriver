#https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = ptr2 = head
        
        while (ptr2 != None and ptr2.next != None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            
        return ptr1
