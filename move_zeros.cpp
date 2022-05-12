#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;

/*
analysis:

*/
void moveZeroes(vector<int> &nums)
{
    int pos = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i])
        {
            int value = nums[i];
            nums[i] = 0;
            nums[pos++] = value;
        }
    }
}

// better solution: reduces the number of writes (maxinum n reads, n writes)
void moveZeroes(vector<int> &nums)
{
    for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++)
    {
        if (nums[cur] != 0)
        {
            swap(nums[lastNonZeroFoundAt++], nums[cur]);
        }
    }
}