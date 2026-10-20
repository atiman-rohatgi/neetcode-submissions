# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        - so we check both tress, we do dfs in both of them and compare
            - if the values same or both null continue else return false
        Complexity
            - Time = O(n)
            - Space = O(n)
        """
        
        def dfs(node1, node2):
            #base case
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            #explore
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            #return
            return left and right

        #return
        return dfs(p, q)

