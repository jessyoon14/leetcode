/*
 * @lc app=leetcode id=116 lang=cpp
 *
 * [116] Populating Next Right Pointers in Each Node
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

// DFS
// class Solution
// {
// public:
//     void connect_row(Node *root)
//     {
//         if (!(root->left))
//             return;
//         root->left->next = root->right;
//         connect_row(root->left);
//         connect_row(root->right);
//         connect_cousin(root->left, root->right);
//     }

//     void connect_cousin(Node *left, Node *right)
//     {
//         if (!(left->right))
//             return;
//         left->right->next = right->left;
//         connect_cousin(left->right, right->left);
//     }

//     Node *connect(Node *root)
//     {
//         if (!root)
//             return root;
//         connect_row(root);
//         return root;
//     }
// };

// Cleaner DFS solution (by KJY)
class Solution
{
public:
    Node *connect(Node *root)
    {
        if (!root || !(root->left))
            return root;

        root->left->next = root->right;
        root->right->next = root->next ? root->next->left : nullptr;
        connect(root->left);
        connect(root->right);
        return root;
    }
};

// @lc code=end
