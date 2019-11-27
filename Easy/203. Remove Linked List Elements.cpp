/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *removeElements(ListNode *head, int val) {
        ListNode *preHead = new ListNode(0);
        preHead->next = head;

        ListNode *preNode = preHead;
        while(preNode->next){
            if(preNode->next->val == val){
                preNode->next = preNode->next->next;
            }else{
                preNode = preNode->next;
            }
        }
        return preHead->next;
    }
};