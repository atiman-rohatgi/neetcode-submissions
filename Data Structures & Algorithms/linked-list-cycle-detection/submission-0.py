# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        - we are trying to detect if any cycle or not
            - if there is a cycle then l1, l2(being the faster one) will matchup with l1.
            - we run this
                - if l2 reaches null then no cycle
                - otherwise if the nodes match up then cycle 
        - edge case
        - complexity
            - Time = O(n)
            - Space = O(1)
        """

        #edge - if empty or only 1
        if not head or not head.next:
            return False
    
        #two pointers
        slow, fast = head, head

        #run the loop while fast and it's next exist - otherwise crash
        #checking if not None, else automatically return False
        while fast and fast.next:
            slow = slow.next        #+1
            fast = fast.next.next   #+2

            if slow == fast:
                return True
            
        return False
        