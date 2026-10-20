# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        - we are arranging the nodes
        - have two pointers which run from front and back till they meet
            - we keep iterating between then and reconnecting the next pointers.
            - since this is SLL, we need to find a middle
            - reverse the other half and then iterate, as SLL cant reverse iterate.
        - complexity
            - Time = O(n)
            - Space = O(1)
        """
        #edge
        if not head or not head.next:
            return

        #find mid
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        #reverse
        prev = None
        curr = mid

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #iterate and add
        first = head
        second = prev

        while second.next:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

