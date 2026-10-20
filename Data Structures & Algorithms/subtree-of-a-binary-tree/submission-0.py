# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        - recusively call diff roots and compare if equal,
            - then use the same trees algo
        - complexity
            - time = O(n x m)
            - space = O(n + m)
        """
        
        #comparision function
        def dfs(node1, node2):
            #base
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
            return left and right # returns true if both are true else false
        
        #root selection function
        def rootSelector(r, sub):
            #base
            if not sub:
                return True
            if not r:
                return False
            
            

            #explore
            if dfs(r, sub) == True:
                return True
            else:
                left = rootSelector(r.left, sub)
                right = rootSelector(r.right, sub)

            #return
            return left or right

        return rootSelector(root, subRoot)

        

