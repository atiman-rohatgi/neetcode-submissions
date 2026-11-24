# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        - we are writing down the btree
        - if left missing then (), else nothing
        - the order needs to be in parenthesis
        - we will use dfs recursion
            - if both not l and r then close
            - if not right then add left
            - if right then add left regardless + right
        - complexity
            - time = O(n)
            - space = O(n)
        """
        
        #function
        def dfs(node):
            #base
            if not node:
                return ""
            if not node.left and not node.right:
                return str(node.val)
            if not node.right:
                return str(node.val) + "(" + dfs(node.left) + ")"
            else:
                return str(node.val) + "(" + dfs(node.left) + ")" + "(" + dfs(node.right) + ")"

        #main
        return dfs(root)
