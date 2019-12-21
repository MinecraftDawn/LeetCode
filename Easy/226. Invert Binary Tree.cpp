/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        swapChild(root);
		return root;
    }

	void swapChild(TreeNode* node){
		if(node == NULL) return;
		TreeNode* tmp = node->left;
		node->left = node->right;
		node->right = tmp;
		swapChild(node->left);
		swapChild(node->right);
	}
};