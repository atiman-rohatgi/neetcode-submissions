# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - nums is unique
        - at least one node will survive
        - to search in nums, converting nums to set makes it O(1)
        - read every node if in nums or not, if not then move on
            - if yes then prev.next = curr.next and advance
        - edge is if removing the first node, there is no prev, so have a dummy node and track prev and curr and move them accordingly
        - complexity
            - time = O(n)
            - space = O(n)
        """
        
        #set things up
        dummy = ListNode(0)
        dummy.next = head #a node before the current head
        prev = dummy
        curr = head
        nums = set(nums)

        #main loop
        while curr is not None:
            if curr.val in nums:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        #return
        return dummy.next


