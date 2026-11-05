# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #merge function
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - basically sorting a list
        - nodes can be 0, so edge is renturn empty list
        - we will use merge sort
        - complexity
            - time = O(nlogn)
            - space = O(n)
        """
        #base case - if single or no node
        if not head or not head.next:
            return head

        #get mid - we will use fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #two sep lists
        left = head
        right = slow.next
        slow.next = None

        #recursively break down
        left_half = self.sortList(left)
        right_half = self.sortList(right)

        #merge back
        return self.merge(left_half, right_half)
