# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        - first and last nodes cant be critical
        - find critical points
        - find min and max distance b/w their indexes
        - we travserse and compare prev, curr and next to find the critical points
        - track first_crit, prev_crit, min dist
        - edge:
            - return -1 if less than 2 points
        - complexity
            - time = O(n)
            - space = O(1)
        """
        
        #edge (atleast 3 nodes needed)
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        #track states
        prev = head
        curr = head.next
        index = 1

        first_crit = -1
        prev_crit = -1
        min_dist = float("inf")

        #travserse
        while curr.next:
            #check for criticalness
            if(prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                if first_crit == -1: #is this is the first point
                    first_crit = index
                else: #if not the first one then we get min dist
                    min_dist = min(min_dist, index - prev_crit)
                prev_crit = index

            #move
            prev = curr
            curr = curr.next
            index += 1

        #if less than 2 points
        if first_crit == -1 or first_crit == prev_crit:
            return [-1, -1]

        #main return
        max_dist = prev_crit - first_crit
        return [min_dist, max_dist]










