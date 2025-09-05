# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        pre,cur=dummy,head
        while cur:
            if cur.val==val:
                temp=cur.next
                pre.next=temp
                cur.next=None
                cur=temp
            else:
                cur=cur.next
                pre=pre.next
        return dummy.next