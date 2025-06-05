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
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        cur=slow.next
        slow.next=pre=None
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        
        n1,n2=head,pre
        while n2:
            temp1,temp2=n1.next,n2.next
            n1.next,n2.next=n2,temp1
            n1,n2=temp1,temp2

