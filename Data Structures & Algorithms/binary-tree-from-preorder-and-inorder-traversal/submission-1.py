# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        - inorder split tells all the left and right nodes
        - preorder split tells the root node then left and right
        - get the root from pre, locate index on in and then do the slicing
            - inorder = left = [:mid] and right = [mid+1:]
            - preorder = left = [1:mid+1] and right = [mid+1:]
        - use hashmap to store indexes, since preoder is sequential ir dont need storage but inorder required to get the mid in O(1) time.
        - complexity
            - time = O(n)
            - space = O(n)
        """
        #base case
        if not preorder or not inorder:
            return None

        #hashmap to store
        map = {} #num : index
        for i in range(0, len(inorder)):
            map[inorder[i]] = i

        self.pre_idx = 0 #starting index

        #dfs function to build the tree
        def dfs(l, r):
            #base
            if l > r:
                return None

            #explore
            #getting the current root node
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            #getting the mid - get l and r
            mid = map[root_val]

            #left and right
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)

            #return
            return root
        
        #return
        return dfs(0, len(inorder)-1)


