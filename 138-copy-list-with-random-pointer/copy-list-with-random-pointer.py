"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p=head
        while p:
            copy=Node(p.val)
            copy.next=p.next
            p.next=copy
            p=copy.next
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            p=p.next.next
            
        dummy=Node(0)
        p1,p2=head,dummy
        while p1:
            copy=p1.next
            p1.next=copy.next
            p2.next=copy
            p1=p1.next
            p2=p2.next
        return dummy.next