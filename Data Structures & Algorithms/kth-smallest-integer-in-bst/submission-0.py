# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        - we are trying to find the kth smallest value
        - min value would be left most child, then node, then right
        - so we need to get the kth
        - using stack we make all left, then pop them out and add right
        - complexity
            - time = 
            - space = 
        """

        stack = []
        curr = root

        while stack or curr:
            #left most exploration
            while curr:
                stack.append(curr)
                curr = curr.left

            #poping of the stack
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            #exploring right of that node
            curr = curr.right


        