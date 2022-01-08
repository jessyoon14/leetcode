#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;

void rotate(vector<int> &nums, int k)
{
    k = k % nums.size();
    if (k == 0)
        return;
    rotate(nums, 0, nums.size(), k);
}

// NOTE: right boundaries not inclusive
void rotate(vector<int> &nums, int left, int right, int k)
{
    printf("In rotate, left: %i, right: %i, k: %i \n", left, right, k);
    if (left >= right - 1)
        return;

    if (k * 2 == right - left)
    {
        swapSegments(nums, left, right - k, k);
    }

    else if (k > (right - left) / 2)
    {
        printf("right is longer \n");
        int swapLength = right - left - k;
        swapSegments(nums, left, right - swapLength, swapLength);
        rotate(nums, left, right - swapLength, right - left - swapLength * 2);
    }

    else
    {
        printf("left is longer\n");
        swapSegments(nums, right - 2 * k, right - k, k);
        rotate(nums, left, right - k, k);
    }
}

// swap nums[left:left+k] with nums[right:right+k]
void swapSegments(vector<int> &nums, int left, int right, int k)
{
    printf("in swap, left: %i, right: %i, k: %i\n", left, right, k);
    int temp;
    for (int i = 0; i < k; i++)
    {
        printf("i: %i\n", i);
        temp = nums[right + i];
        nums[right + i] = nums[left + i];
        nums[left + i] = temp;
    }
}