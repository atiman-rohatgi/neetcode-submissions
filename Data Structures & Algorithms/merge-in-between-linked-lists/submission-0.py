# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - replace nodes from list1 index (a-b) with list2
        - two pass, one removes the nodes from list1, the next pass we append list 2 to the boundry node
        - locate (a-1) and (b+1) nodes
        - connect (a-1).next to list2 and that to (b+1)
        - complexity
            - time = O(n)
            - space = O(1)
        """

        #getting (a-1)
        prev_a = list1
        for _ in range(0, a-1):
            prev_a = prev_a.next

        #getting (b+1)
        after_b = list1
        for _ in range(0, b+1):
            after_b = after_b.next

        #connecting
        prev_a.next = list2
        
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        tail2.next = after_b

        #return
        return list1