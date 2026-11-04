# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        - reverse LL
        - index starts from one
        - edge: l and r be equal
        - there will be three parts: before the left, l to r and after r
            - before l and after r stay the same
            - b/w l and r gets reversed
            - left_prev needed and the prev will become tail
        - complexity
            - time = O(n)
            - space = O(1)
        """
        #edge if l, r equal
        if left == right:
            return head

        #set things up
        dummy = ListNode(0)
        dummy.next = head #extending the main list to handle left == 1
        left_prev = dummy

        #before l - moving till the middle part
        for _ in range(0, left-1):
            left_prev = left_prev.next

        #middle (reversal)
        curr = left_prev.next
        prev = None

        for _ in range(0, right-left+1):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        #connect things
        left_prev.next.next = curr #connecting tail from none to after r
        left_prev.next = prev #the reversed head before r

        #return
        return dummy.next
        