#Leetcode remove Nth node from the end of the list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
 def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

  dummy = ListNode(0, head)
  left = dummy
  right = head

  while n > 0 and right: # this is to iterate right to be n+1 positions ahead of left(we use loop since right = head + n
     right = right.next  # wont work
     n -= 1
     # this ensures that when right runs out we know that left is on the nTh - 1 position from the
                   # end of the list so we can simply assign the .next to = .next.next


  while left and right:
   left = left.next
   right = right.next

  left.next = left.next.next #this is to break the connection
  # 1 -> 2 -> 3 -> 4 -> 5  output = 1 -> 2 -> 3 -> 5
  
  return dummy.next