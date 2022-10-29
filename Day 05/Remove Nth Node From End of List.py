#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if (head.next == None):
        #     #n = 1. delete the only elem
        #   ''' This case covered when n == sizeof LL
        #   '''
        #     return None
        
        
        ptr1 = head
        ptr2 = ptr1
        
        for _ in range(n):
            ptr2 = ptr2.next
            
        if (ptr2 == None):
            #i.e., n = size of LL
            #i.e., delete first node
            return head.next
            
        while(ptr2.next):
            ptr1, ptr2 = ptr1.next, ptr2.next
            
        ptr1.next = ptr1.next.next
        
        return head
