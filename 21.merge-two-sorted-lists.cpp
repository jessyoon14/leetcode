/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
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

// Attempt 2: cleaner code without tail recursion
class Solution {
   public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) return list2;
        if (!list2) return list1;

        if (list1->val < list2->val) {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};

// Attempt 1: use tail recursion
// class Solution {
//    public:
//     void merge(ListNode* list1, ListNode* list2, ListNode* acc) {
//         if (!list1) {
//             acc->next = list2;
//             return;
//         }
//         if (!list2) {
//             acc->next = list1;
//             return;
//         }
//         if (list1->val < list2->val) {
//             acc->next = list1;
//             merge(list1->next, list2, list1);
//         } else {
//             acc->next = list2;
//             merge(list1, list2->next, list2);
//         }
//     }

//     ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
//         if (!list1) return list2;
//         if (!list2) return list1;

//         if (list1->val < list2->val) {
//             merge(list1->next, list2, list1);
//             return list1;
//         } else {
//             merge(list1, list2->next, list2);
//             return list2;
//         }
//     }
// };

// @lc code=end
