# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        - we will use dfs to traverse the deeepest nodes and reverse their order
        - go all the way to bottom till none, and reverse the nodes and go up
        - Complexity
            - Time = O(n)
            - Space = O(n)
        
        """
        def dfs(node):
            #base case
            if not node:
                return None

            #order of exploration
            dfs(node.left)  #on left
            dfs(node.right) #on right

            #swap
            node.left, node.right = node.right, node.left
            return node

        #return
        return dfs(root)