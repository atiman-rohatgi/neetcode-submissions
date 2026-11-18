class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        - we are basically creating a binary tree, with the input
        - if isleft == 1, then left else right, add as child node
        - output should be the head node
        - since input can be any order, two dict parent and child
            - the node not in child is the root node
        - complexity
            - time = O(n)
            - space = O(n)
        """

        nodes = {} #all the nodes that we've seen so far
        children = set() #the child nodes to gett the root node

        #iterating through all and adding to the seen dict
        for parent, child, isleft in descriptions:
            if parent not in nodes: #if parent visited or not
                nodes[parent] = TreeNode(parent)
            if child not in nodes: # if child seen or not
                nodes[child] = TreeNode(child)

            #adding the child to left ro right
            if isleft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            children.add(child) #add to the children set

        #now figure out the root node
        for val in nodes:
            if val not in children:
                return nodes[val]




