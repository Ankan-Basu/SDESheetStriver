#https://leetcode.com/problems/reverse-linked-list/

## ITERATIVE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        prevPtr = None
        currPtr = head
        nextPtr = currPtr.next
        
        while True:
            currPtr.next = prevPtr
            prevPtr = currPtr
            currPtr = nextPtr
            if (currPtr == None):
                break
            nextPtr = nextPtr.next
            
            
        #head = prevPtr
        return prevPtr
    
    
#maybe better
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if head == None:
        #    return None
        #already handled in currPtr != None of while loop
        
        prevPtr = None
        currPtr = head
        nextPtr = None
        
        while currPtr:
            nextPtr = currPtr.next
            currPtr.next = prevPtr
            prevPtr = currPtr
            currPtr = nextPtr
            
        #head = prevPtr
        return prevPtr
