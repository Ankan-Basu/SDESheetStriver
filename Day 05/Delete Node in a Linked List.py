#https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

"""
Delete given node in O(1)
Head not given
just copy val of next node into curr node 
and delete next node
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
