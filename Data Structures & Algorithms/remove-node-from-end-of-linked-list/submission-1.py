# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - we can use a two pass approach
            - first to calculate the len (N)
            - then getting the number at index (N - n) and rewire it
        - Complexity
            - Time = O(n)
            - Space = O(1)
        """
        #getting the length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        #the index calculation
        target_idx = length - n

        #edge case - if removing the head node
        if target_idx == 0:
            return head.next

        #rewiring
        idx = 0
        curr = head
        while idx != (target_idx-1):
            curr = curr.next
            idx += 1
        curr.next = curr.next.next

        #return head
        return head
        
        
