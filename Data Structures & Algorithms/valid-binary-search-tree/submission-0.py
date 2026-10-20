# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        - recursively dfs to check check the nodes, return true if all return true
        - we check while node, if left is smaller and right is bigger
            - and then go deeper on each node
        - we track a max for left side and min for right side and check the nodes against that
            - so can just have an interval, which allows one single function to be used
        - complexity
            - time = O(n)
            - space = O(h)
        """

        #dfs
        def dfs(node, low, high):
            #base
            if not node:
                return True

            if not (low < node.val < high):
                return False

            #explore
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            #return 
            return left and right

        #return
        return dfs(root, float("-inf"), float("inf"))


        