#https://leetcode.com/problems/rotate-list/

#Normal Break and Join
#Scroll down for circular LL method

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr1 = head
        size_list = 0
        
        while(ptr1):
            size_list += 1
            ptr1 = ptr1.next
            
        if size_list == 0:
            return None
            
        k = k % size_list
        
        if k == 0:
            return head
        
        ptr1 = ptr2 = head
        
        for _ in range(k):
            ptr2 = ptr2.next
            
        while(ptr2.next):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        new_head = ptr1.next
        ptr1.next = None
        ptr2.next = head
        
        return new_head
        
        
        
        
#Making Circular LL
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr1 = head
        size_list = 0
        
        while(ptr1):
            size_list += 1
            ptr1 = ptr1.next
            
        if size_list == 0:
            return None
            
        k = k % size_list
        
        if k == 0:
            return head
        
        ptr2 = head
        
        while(ptr2.next):
            ptr2 = ptr2.next
            
        ptr2.next = head
        
        ptr3 = head
        
        for _ in range(size_list - k):
            ptr3 = ptr3.next
            ptr2 = ptr2.next
            
        ptr2.next = None
        
        return ptr3
