# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head
        dummy = ListNode(0, head)
        p1 = dummy

        while True:
            p2 = p1
            for _ in range(k):
                p2 = p2.next
                if not p2:
                    return dummy.next

            a = p1.next
            b = a.next
            for _ in range(k - 1):
                a.next = b.next
                b.next = p1.next
                p1.next = b
                b = a.next

            p1 = a