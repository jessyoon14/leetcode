#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int> &numbers, int target)
{
    int left = 0;
    int right = numbers.size() - 1;

    while (left < right)
    {
        int left_value = numbers[left];
        int right_value = numbers[right];

        int sum = left_value + right_value;

        if (sum == target)
            break;
        else if (sum > target)
            right--;
        else // sum < target
            left++;
    }

    return {left++, right++};
}
