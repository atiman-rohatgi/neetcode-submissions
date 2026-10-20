# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque #deque import
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        - we will use bfs to do level by level
        - have a deque, create a level list, where we append all the nodes per level
        - append that level list to the res list
        - Complexity
            - time = O(n)
            - space = O(n)
        """
        # base
        if not root:
            return []

        #bfs
        #setting thigs up
        res = []
        queue = deque([root])
        
        #the queue process
        #level wise adding nodes and poping them to add to the level list
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                #left and right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #appending the level list to the res list
            res.append(level)
        
        #return the res list
        return res


