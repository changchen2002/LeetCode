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
        while p:  #为什么不while p and p.next? 因为有p就有p.next
            q.next=p.next
            p.next=p.next.next
            p,q=p.next,q.next
        return dummy.next
