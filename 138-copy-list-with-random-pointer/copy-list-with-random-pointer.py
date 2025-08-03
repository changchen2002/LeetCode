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
        p=head
        while p:
            new=Node(p.val)
            new.next=p.next
            p.next=new
            p=new.next
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            p=p.next.next
        dummy=Node(0)
        p,q=head,dummy
        while p:
            q.next=p.next
            p.next=p.next.next
            p=p.next
            q=q.next
        return dummy.next