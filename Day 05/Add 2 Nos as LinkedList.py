#https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        dummyHead = ListNode()
        ptr3 = dummyHead
        
        carry_dig = 0
        while (ptr1 and ptr2):
            curr_sum = ptr1.val + ptr2.val + carry_dig #prev carry
            sum_dig = curr_sum % 10
            carry_dig = curr_sum // 10
            ptr3.next = ListNode(sum_dig)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            ptr3 = ptr3.next
            
        while (ptr1):
            curr_sum = ptr1.val + carry_dig
            sum_dig = curr_sum % 10
            carry_dig = curr_sum // 10
            ptr3.next = ListNode(sum_dig)
            ptr1 = ptr1.next
            ptr3 = ptr3.next
            
        while(ptr2):
            curr_sum = ptr2.val + carry_dig
            sum_dig = curr_sum % 10
            carry_dig = curr_sum // 10
            ptr3.next = ListNode(sum_dig)
            ptr2 = ptr2.next
            ptr3 = ptr3.next
            
        if (carry_dig != 0):
            ptr3.next = ListNode(carry_dig)
            
        return dummyHead.next
