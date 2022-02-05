/*
 * @lc app=leetcode id=82 lang=cpp
 *
 * [82] Remove Duplicates from Sorted List II
 */

// @lc code=start
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *left = nullptr, *right = head;

        while (right) {
            int count = 0;
            int val = right->val;

            while (right && right->val == val) {
                right = right->next;
                count++;
            }

            if (count > 1) {
                if (left)
                    left->next = right;
                else
                    head = right;
            } else
                left = left ? left->next : head;
        }

        return head;
    }
};
// @lc code=end