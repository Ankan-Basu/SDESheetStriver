#https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, curr_head, end):
        if (curr_head == end or curr_head.next == end):
            return curr_head
        
        new_head = self.reverse(curr_head.next, end)
        next_head = curr_head.next
        next_head.next = curr_head
        curr_head.next = None
        
        return new_head
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr1 = ptr2 = head
        dummy_head = ListNode()
        tmp = dummy_head
        
        while(True):
            out_of_bounds = False
            for _ in range(k):
                if (ptr2 == None):
                    out_of_bounds = True
                    break

                ptr2 = ptr2.next
                
            if out_of_bounds:
                tmp.next = ptr1
                break

            new_head = self.reverse(ptr1, ptr2)
            tmp.next = new_head
            tmp = ptr1
            ptr1 = ptr2
            
        return dummy_head.next
