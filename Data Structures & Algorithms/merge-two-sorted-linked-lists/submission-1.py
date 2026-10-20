# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - we are trying to merge two sorted lists
            - have three pointers run out two on each list and one on the res list
            - egde cases
                - if both null or either is null
        - complexity
            - time = O(m + n)
            - space = O(m + n)
        """
        
        #edge
        if not list1:
            return list2
        if not list2:
            return list1

        #setting things ups
        l1 = list1
        l2 = list2
        res = ListNode()
        curr = res

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

        while l2:
            curr.next = l2
            l2 = l2.next 
            curr = curr.next

        #return
        return res.next #as head gets initilaized to 0
        