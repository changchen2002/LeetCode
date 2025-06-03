# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        count=0 #add count as a second parameter for comparing when values are equal
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val,count,l))
                count+=1
        dummy=ListNode(0)
        cur=dummy
        while heap:
            val,_,node=heapq.heappop(heap)
            cur.next=node
            cur=cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val,count,node.next))
                count+=1
        return dummy.next


        

        