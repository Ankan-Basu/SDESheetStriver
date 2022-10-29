#https://leetcode.com/problems/intersection-of-two-linked-lists/

#Lengthy
#Scroll down for cleaner code (same Time and Space Complexity)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB
        
        sizeA = sizeB = 0
        
        while (ptr1 and ptr2):
            sizeA += 1
            sizeB += 1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        while(ptr1):
            sizeA += 1
            ptr1 = ptr1.next
            
        while(ptr2):
            sizeB += 1
            ptr2 = ptr2.next
            
        ptr1, ptr2 = headA, headB
        
        if (sizeA > sizeB):
            diff = sizeA - sizeB
            for _ in range(diff):
                ptr1 = ptr1.next
                
        
        elif (sizeA < sizeB):
            diff = sizeB - sizeA
            for _ in range(diff):
                ptr2 = ptr2.next
                
        while (ptr1 and ptr2 and ptr1 != ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1
      
      
#More Elegant
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB
        
        while (ptr1 != ptr2):
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA
            
        return ptr1
