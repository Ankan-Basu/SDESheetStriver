#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, curr_head):
        if (curr_head == None or curr_head.next == None):
            return curr_head
        
        new_head = self.reverse_list(curr_head.next)
        
        next_head = curr_head.next
        next_head.next = curr_head
        curr_head.next = None
        
        return new_head
        
    
    def find_middle(self, head):
        fast_ptr = slow_ptr = head
        
        while (fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
        return slow_ptr
    
    def print_list(self, head):
        ptr = head
        while(ptr):
            print(ptr.val, end=' ')
            ptr = ptr.next
        print()
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head2 = self.find_middle(head)
        
        new_head =self.reverse_list(head2)
        
        ptr1, ptr2 = head, new_head
        
        is_palind = True
        
        while (ptr1 and ptr2):
            if (ptr1.val != ptr2.val):
                is_palind =  False
                break
            ptr1 = ptr1.next
            ptr2 = ptr2.next
                
        return is_palind
