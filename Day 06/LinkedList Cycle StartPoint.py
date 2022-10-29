#https://leetcode.com/problems/linked-list-cycle-ii/

#Floyd's Cycle Detection Algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_ptr = slow_ptr = head
        
        cycle_found = False
        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if (slow_ptr == fast_ptr):
                cycle_found = True
                break
                
        if not cycle_found:
            return None
        
        fast_ptr = head
        
        while(fast_ptr != slow_ptr):
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
            
        return slow_ptr
