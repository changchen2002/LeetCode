# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        cur=slow.next
        slow.next=None
        pre=None
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        
        first,second=head,pre
        while second:
            n1,n2=first.next,second.next
            first.next,second.next=second,n1
            first,second=n1,n2
        

