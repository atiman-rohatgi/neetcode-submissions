# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        - we are trying to get the depth
        - we will be using dfs
        - Complexity
            - Time = O(n)
            - Space = O(h)
        """
        
        def dfs(node):
            #base case
            if not node:
                return 0

            #order
            left = dfs(node.left)
            right = dfs(node.right)

            #return agg
            return (1 + max(left, right))

        #dfs on the root node
        return dfs(root)