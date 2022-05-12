// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution
{
public:
    int firstBadVersion(int n)
    {
        unsigned int lower_bound = 0;
        unsigned int upper_bound = n;

        while (lower_bound <= upper_bound)
        {
            unsigned int middle_index = (lower_bound + upper_bound) / 2;
            bool is_bad = isBadVersion(middle_index);

            if (is_bad)
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

// alternate solution
class Solution
{
public:
    int firstBadVersion(int n)
    {
        unsigned int lower_bound = 0;
        unsigned int upper_bound = n;

        while (lower_bound < upper_bound)
        {
            unsigned int middle_index = (lower_bound + upper_bound) / 2;
            bool is_bad = isBadVersion(middle_index);

            if (is_bad)
            {
                upper_bound = middle_index;
            }
            else
            {
                lower_bound = middle_index + 1;
            }
        }

        return lower_bound;
    }
};