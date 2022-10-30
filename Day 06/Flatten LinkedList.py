#https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def merge_lists(head1, head2):
    ptr1, ptr2 = head1, head2
    dummy_head = Node(0)
    ptr3 = dummy_head
    
    head1.next = None
    
    while(ptr1 and ptr2):
        if (ptr1.data < ptr2.data):
            ptr3.bottom = ptr1
            ptr1 = ptr1.bottom
        else:
            ptr3.bottom = ptr2
            ptr2 = ptr2.bottom
            
        ptr3 = ptr3.bottom
        
    #elem left in List1
    while(ptr1):
        ptr3.bottom = ptr1
        ptr1 = ptr1.bottom
        ptr3 = ptr3.bottom
        
    #elem left in List2
    while(ptr2):
        ptr3.bottom = ptr2
        ptr2 = ptr2.bottom
        ptr3 = ptr3.bottom
        
    return dummy_head.bottom
    
def flatten(root):
    #Your code here
    if (root.next == None):
        return root
        
    head2 = flatten(root.next)
    new_head = merge_lists(root, head2)
    return new_head
