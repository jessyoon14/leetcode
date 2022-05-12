class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int lower_bound = 0;
        int upper_bound = nums.size() - 1;

        while (lower_bound <= upper_bound)
        {
            int middle_index = (lower_bound + upper_bound) / 2;
            int middle_value = nums[middle_index];

            if (middle_value == target)
            {
                return middle_index;
            }
            else if (middle_value > target)
            {
                upper_bound = middle_index - 1;
            }
            else
            {
                lower_bound = middle_index + 1;
            }
        }

        return lower_bound;
    }
};