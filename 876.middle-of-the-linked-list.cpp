/*
 * @lc app=leetcode id=876 lang=cpp
 *
 * [876] Middle of the Linked List
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

/**
 * NOTE: the while() below is equivalent to:
    while (1)
    {
        right = right->next;
        if (right)
        {
            right = right->next;
            left = left->next;
            if (!right) // odd number of nodes
                return left;
        }
        else
            return left;
    }
 */

class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {
        /**
         * Each iteration, left pointer is updated by one, right pointer is updated by two
         *
         */
        ListNode *left = head, *right = head;

        right = head->next;
        while (right)
        {
            right = right->next;
            left = left->next;
            if (!right)
                break;
            right = right->next;
        }

        return left;
    }
};

// @lc code=end
