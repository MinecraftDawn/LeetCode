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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode();
		ListNode *run = head;
		int carry = 0;
		
		while(l1 && l2){
			int add = (l1->val + l2->val + carry) % 10;
			run->next = new ListNode();
			run = run->next;
			run->val = add;
			
			carry = (l1->val + l2->val + carry) / 10;
			l1 = l1->next;
			l2 = l2->next;
		}
		
		while(l1){
			int add = (l1->val + carry) % 10;
			run->next = new ListNode();
			run = run->next;
			run->val = add;
			
			carry = (l1->val + carry) / 10;
			l1 = l1->next;
		}
		
		while(l2){
			int add = (l2->val + carry) % 10;
			run->next = new ListNode();
			run = run->next;
			run->val = add;
			
			carry = (l2->val + carry) / 10;
			l2 = l2->next;
		}
		
		if(carry > 0){
			run->next = new ListNode();
			run = run->next;
			run->val = carry;
		}
		
		return head->next;
    }
};