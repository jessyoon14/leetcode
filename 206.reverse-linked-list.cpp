/*
 * @lc app=leetcode id=206 lang=cpp
 *
 * [206] Reverse Linked List
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
    ListNode* reverseNode(ListNode* prev, ListNode* curr) {
        if (!prev || !curr) return prev;
        ListNode* next = curr->next;
        curr->next = prev;
        return reverseNode(curr, next);
    }

    ListNode* reverseList(ListNode* head) {
        if (!head) return head;
        ListNode* next = head->next;
        head->next = nullptr;
        return reverseNode(head, next);
    }
};
// @lc code=end
