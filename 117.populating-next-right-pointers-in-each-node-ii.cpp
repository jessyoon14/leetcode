/*
 * @lc app=leetcode id=117 lang=cpp
 *
 * [117] Populating Next Right Pointers in Each Node II
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
   private:
    void connectLevel(Node* node) {
        Node* curr = node->left ? node->left : node->right;

        while (!curr && node->next) {
            node = node->next;
            curr = node->left ? node->left : node->right;
        }

        if (!curr || !node) return;

        Node* leftmostChild = curr;

        while (curr) {
            if (curr != node->right && node->right) {
                curr->next = node->right;
                curr = curr->next;
            } else {
                if (!node->next) break;
                node = node->next;
                if (node->left) {
                    curr->next = node->left;
                    curr = curr->next;
                } else if (node->right) {
                    curr->next = node->right;
                    curr = curr->next;
                }
            }
        }

        connectLevel(leftmostChild);
    }

   public:
    Node* connect(Node* root) {
        if (!root || !(root->left || root->right)) return root;

        connectLevel(root);

        return root;
    }
};
// @lc code=end
