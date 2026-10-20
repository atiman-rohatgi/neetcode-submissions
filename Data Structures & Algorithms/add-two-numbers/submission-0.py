# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - non negative
        - length dont need to be same
        - node can be 0-9
        - use a three pointer approach, p1,p2,p3
        - as the lists start from one's place, no reversal is needed
            - but the question allows carry, so ther will be a carry variable
            - you keep mod10 while carry is (//10)
        - iterate till all three reach null, l1, l2 and carry 
        - complexity
            - time = O(n)
            - space = O(n)
        """

        #set things up
        carry = 0
        l3 = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = l3
        
        #main loop
        while p1 != None or p2 != None or carry != 0:
            #calculate the vals
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            
            total = v1+v2+carry
            node_val = total % 10
            carry = total // 10
            
            #create node in the list
            p3.next = ListNode(node_val)
            p3 = p3.next

            #move the nodes
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return l3.next