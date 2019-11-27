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
    ListNode* reverseList(ListNode* head) {
        std::stack<ListNode*> nodes;
		
		ListNode *run = head;
		while(run){
			nodes.push(run);
			run = run->next;
		}
		
		ListNode *preHead = new ListNode(0);
		run = preHead;
		while(!nodes.empty()){
			run->next = nodes.top();
            nodes.pop();
			run = run->next;
		}
		run->next = NULL;
		
		return preHead->next;
    }
};