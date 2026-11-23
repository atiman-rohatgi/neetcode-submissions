"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        - initially all (.next) are null
        - in the order add right to each node, if not then none
        - this is a bfs question, with the only change that each node.next will point to node on the right.
        - if recursive used, then stack space is not counted
            - connect left to right kid for the left
            - connect right to neighbors left kid for the right
            - call this on left and right kid
        - complexity
            - time = O(n)
            - space = O(1)
        """

        def bfs(curr):
            #base case
            if curr is None or not curr.left:
                return

            #recurse
            if curr.left and curr.right:
                curr.left.next = curr.right

            if curr.right and curr.next:
                curr.right.next = curr.next.left

            bfs(curr.left)
            bfs(curr.right)

        #return
        bfs(root)
        return root

        
