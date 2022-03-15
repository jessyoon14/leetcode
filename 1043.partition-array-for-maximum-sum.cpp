/*
 * @lc app=leetcode id=1043 lang=cpp
 *
 * [1043] Partition Array for Maximum Sum
 */

// @lc code=start

/*
pseudocode

make 2D dp array -> I'll start without, since this seems unnecessary
make 1D dp sum array
make last elem count

for curr in array
    if (can reuse last elem && last elem > curr) (use prev)
        # extend tail

    else (need to use curr)
        if curr > last modified array elem (use curr)
        # change tail to curr & update penultimate elements as necessary

        # need to find optimum out of the 3 cases below


        prev2 | prev2 | prev2
        prev2 | prev2 | curr
        prev2 | prev1 | prev1
        prev2 | curr  | curr

        prev1 | prev1 | prev1
        prev1 | prev1 | curr

        curr  | curr  | curr


        generalizing:
        case 1: max is prev1 or prev2

            case 1-A: can extend prev tail -> extend
                prev2 | prev2 | prev2
                prev2 | prev1 | prev1
                prev1 | prev1 | prev1

            case 1-B: cannot extend prev tail
                case i: if last elem > curr
                    sum: (sum-1) + curr
                    prev2 | prev2 | curr
                    prev1 | prev1 | curr
                case ii: prev2 > curr > prev1
                    sum: (sum-2) + curr * 2
                    prev2 | curr  | curr


        case 2: max is curr
            curr  | curr  | curr

        choose max (using prev values of DP)
        to choose max, use sum of last three elem



        /// other method
        generalizing:
        case 1: extend prev tail
            if extendable (prev tail > curr && extendable)
            if not extendable: move

        case 2: use curr as tail
            use curr once
            use curr twice
            use curr three times

        choose max (using prev values of DP)
        to choose max, use sum of last three elem
*/
class Solution {
   public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        // initialize variables & arrays
        int size = arr.size();
        vector<int> sums(size, 0);
        int last_elem;
        int last_elem_index;
        int last_elem_use_count;

        // for loop over array

        // initialize
        sums[0] = arr[0];
        last_elem = arr[0];
        last_elem_use_count = 1;
        last_elem_index = 0;
        for (int i = 1; i < size; i++) {
            // printf("enter for, i: %i\n", i);
            int curr = arr[i];
            int prev = last_elem;
            int max_sum = 0;

            // case 1: extend prev tail
            if (last_elem_use_count < k) {
                // printf("reach a\n");
                // extendable
                max_sum = max(max_sum, sums[i - 1] + last_elem);
                last_elem_use_count++;
            } else {
                // not extendable
                // printf("reach b\n");

                for (int j = max(0, i - k + 1); j <= last_elem_index; j++) {
                    // printf("reach c\n");

                    int max_sum_candidate = sums[j] + last_elem * (i - j);
                    if (max_sum < max_sum_candidate) {
                        max_sum = max_sum_candidate;
                        last_elem_use_count = i - j;
                    }
                    // printf("reach c max: %i\n", max_sum);
                }
            }
            // printf("reach 1\n");

            // case 2: use curr as tail

            for (int j = 1; j <= min(k, i + 1); j++) {
                // printf("reach 2\n");
                int max_sum_candidate;
                if (i + 1 == j) {
                    // printf("case 1\n");
                    max_sum_candidate = curr * j;

                } else {
                    // printf("case 2\n");
                    max_sum_candidate = sums[i - j] + curr * j;
                }
                // printf("reach 3\n");

                if (max_sum < max_sum_candidate) {
                    max_sum = max_sum_candidate;
                    last_elem_use_count = j;
                    last_elem = curr;
                }
                // printf("reach 4\n");
            }

            sums[i] = max_sum;
            // printf("for i: %i, sum: %i\n", i, max_sum);
        }

        return sums[size - 1];
    }
};
// @lc code=end
