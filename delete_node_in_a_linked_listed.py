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
        node.val = node.next.val
        node.next = node.next.next

        #what this does
        # 1 -> 2 -> 3 -> 4 -> 5 if the node we want to delete is 3 , firstly we copy the val after 3 which is 4 so 3 is
        # equal to  4 therefore
        #we have 1 -> 2 -> 4 -> 4 -> 5 now we assign the new 4 to point to the value after the old 4 (which is 5 :) )
        #so at the end we have 1 -> 2 -> 4 -> 5
