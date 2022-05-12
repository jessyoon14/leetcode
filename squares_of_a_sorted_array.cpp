#include <vector>
#include <cmath>

class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        vector<int> squares = sortByAbsoluteValue(nums);

        // square list
        for (int i = 0; i < squares.size(); i++)
        {
            squares[i] = squares[i] * squares[i];
        }
        return squares;
    }

    vector<int> sortByAbsoluteValue(vector<int> &nums)
    {
        vector<int> absSortedNums;

        // if all numbers positive, just square
        if (nums[0] >= 0)
            return nums;

        // all numbers are negative, just reverse
        if (nums[nums.size() - 1] <= 0)
            return reverse(nums);

        // iterate left and right indices and sort
        int right = findFirstPositiveIdx(nums);
        int left = right - 1;

        while (left > -1 && right < nums.size())
        {
            if (abs(nums[left]) < nums[right])
            {
                absSortedNums.push_back(nums[left]);
                left--;
            }
            else
            {
                absSortedNums.push_back(nums[right]);
                right++;
            }
        }

        // add leftover negative numbers
        while (left > -1)
        {
            absSortedNums.push_back(nums[left]);
            left--;
        }

        // add leftover positive numbers
        while (right < nums.size())
        {
            absSortedNums.push_back(nums[right]);
            right++;
        }

        return absSortedNums;
    }

    int findFirstPositiveIdx(vector<int> &nums)
    {
        // find index of first positive number
        int left = 0;
        int right = nums.size() - 1;

        while (left < right)
        {
            int middle = left + (right - left) / 2;

            if (nums[middle] >= 0)
                right = middle;
            else
                left = middle + 1;
        }
        return left;
    }

    vector<int> reverse(vector<int> &nums)
    {
        // reverse list
        int len = nums.size();
        for (int i = 0; i < len / 2; i++)
        {
            int temp = nums[i];
            nums[i] = nums[len - 1 - i];
            nums[len - 1 - i] = temp;
        }
        return nums;
    }
};