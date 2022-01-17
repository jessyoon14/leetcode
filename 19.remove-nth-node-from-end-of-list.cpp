/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
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
class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *left = head, *right = head;

        for (int i = 0; i < n; i++)
            right = right->next;

        if (!right)
            return left->next;

        right = right->next;

        while (right)
        {
            right = right->next;
            left = left->next;
        }

        ListNode *nthNode = left->next;
        left->next = nthNode->next;
        return head;
    }
};
// @lc code=end
