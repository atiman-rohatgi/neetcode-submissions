# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - not reversed
        - non negative, (0,9)
        - len of l1 !- len l2
        - usiung stack add nodes and process them while popping
            - if one stack is empty, the just replace that with 0 in calculations
        - Complexity
            - time = O(n+m)
            - space = O(n+m)
        """
        
        #build the strcutures
        s1 = []
        s2 = []

        #fill the stack
        curr = l1
        while curr:
            s1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            s2.append(curr.val)
            curr = curr.next

        #process the nodes
        carry = 0
        head = None

        while s1 or s2 or carry:
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            #keep connecting new node to the start
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        #output
        return head