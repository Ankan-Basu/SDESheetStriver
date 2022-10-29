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
    
    
    
#RECURSIVE
class Solution:
    def reverse_recur(self, head):
        if (head == None or head.next == None):
            return head
        
        new_head = self.reverse_recur(head.next) 
        #will go deep till end and return the last node as head
        
        #find the next node from the curr node
        next_node = head.next
        
        #link next of next node to the curr (head)
        next_node.next = head
        
        #link next of curr node to null
        head.next = None
        
        return new_head
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        return self.reverse_recur(head)
