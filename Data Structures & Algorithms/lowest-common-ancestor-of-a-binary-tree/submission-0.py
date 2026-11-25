# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - have to return the most common parent node, can be itself
        - p and q are unique and will always exist
        - all nodes vals are unique
        - we will use dfs, where the bottom node will return of they found p or q
            - so instead of having two paths and finding out the common we can use this recursive algo
            - once both found it will keep returning that upstairs.
        - complexity
            - time = O(n)
            - space = O(n)
        """
        
        #dfs
        def dfs(node, p, q):
            #base
                #if none then just cut the loop
                #if either node found then anyways LCA so no need to go deeper
            if not node or node == p or node == q:
                return node

            #explore
            left = dfs(node.left, p, q)
            right = dfs(node,right, p, q)

            #return
            return 

        #main