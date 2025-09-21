/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head) return NULL;
        ListNode dummy(0,head);
        ListNode* pre=&dummy, *cur=head;
        
        for (int i=0;i<left-1;i++){
            pre=pre->next;
        }
        cur=pre->next;
        ListNode* start=nullptr;
        for (int i=0;i<right-left+1;i++){
            ListNode* tmp=cur->next;
            cur->next=start;
            start=cur;
            cur=tmp;
        }
        pre->next->next=cur;
        pre->next=start;
        return dummy.next;  //对象的值是. 指针的值是->
    }
};