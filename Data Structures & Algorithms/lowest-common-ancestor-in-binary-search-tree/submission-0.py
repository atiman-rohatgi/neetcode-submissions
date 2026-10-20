# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        - we are trying to find the lowest common parent of p and q
        - since this is a BST, left would be smaller while right would be bigger.
        - if curr node is b/w p and q, hence a split, hence LCA.
        - if curr node is == to either p or q, hence LCA
        - if both bigger or smaller we go right or left respectively.
        - Complexity
            - time = O(h)
            - space = O(1)
        """
        
        curr = root

        while curr:
            #if in between or one is equal
            if (p.val < curr.val < q.val) or (q.val < curr.val < p.val) or (p.val == curr.val) or (q.val == curr.val):
                return curr
            #if both big or small
            elif (p.val >= curr.val) and (q.val >= curr.val):
                curr = curr.right
            elif (p.val <= curr.val) and (q.val <= curr.val):
                curr = curr.left







