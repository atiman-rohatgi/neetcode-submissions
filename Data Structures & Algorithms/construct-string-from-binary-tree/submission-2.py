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
        - or we can use normal stack + dfs + seen set
            - have two loops one for adding another for closing parenthesis
        - complexity
            - time = O(n)
            - space = O(n)
        """
        #edge
        if not root:
            return ""

        #set things up
        stack = [root]
        visited = set()
        res = []

        #stack
        while stack:
            curr = stack[-1]

            if curr in visited:
                stack.pop()
                res.append(")")
            else:
                visited.add(curr)
                res.append("("+str(curr.val))

                if not curr.left and curr.right:
                    res.append("()")
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

        return "".join(res)[1:-1]
        
