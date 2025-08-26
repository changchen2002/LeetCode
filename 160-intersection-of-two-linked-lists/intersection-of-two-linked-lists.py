# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashset=set()
        p=headA
        while p:
            hashset.add(p)
            p=p.next
        q=headB
        while q:
            if q in hashset:
                return q
            q=q.next
        return None