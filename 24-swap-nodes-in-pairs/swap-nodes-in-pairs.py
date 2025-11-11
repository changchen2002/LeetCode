# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0,head)
        p1=head
        prev=dummy
        while p1 and p1.next:
            p2=p1.next
            nxt=p2.next
            p2.next=p1
            p1.next=nxt
            prev.next=p2
            prev=p1
            p1=nxt
        return dummy.next
        