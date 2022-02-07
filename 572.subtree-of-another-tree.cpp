/*
 * @lc app=leetcode id=572 lang=cpp
 *
 * [572] Subtree of Another Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
   private:
    bool checkNode(TreeNode* root, TreeNode* subRoot) {
        if (!root && !subRoot) return true;
        if (!root || !subRoot) return false;
        if (root->val == subRoot->val)
            return (checkNode(root->left, subRoot->left) && checkNode(root->right, subRoot->right));
        else
            return false;
    }

   public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        queue<TreeNode*> nextLevel;
        nextLevel.push(root);
        TreeNode* curr;

        while (!nextLevel.empty()) {
            curr = nextLevel.front();
            nextLevel.pop();
            if (checkNode(curr, subRoot))
                return true;
            if (curr->left)
                nextLevel.push(curr->left);
            if (curr->right)
                nextLevel.push(curr->right);
        }

        return false;
    }
};
// @lc code=end
