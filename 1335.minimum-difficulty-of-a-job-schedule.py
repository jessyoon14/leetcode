#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
class Solution:
    """
    Bottom-up Dynamic programming
    Time complexity: O((n - d)^2 * d)
    Space complexity: O(n * d)
    """

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[1][-1] = jobDifficulty[-1]
        for i in range(n - 1, -1, -1):
            dp[1][i] = max(jobDifficulty[i], dp[1][i+1])

        for days_left in range(2, d + 1):
            max_start_index = n - days_left
            for start_index in range(max_start_index, -1, -1):
                today_difficulty = 0
                for i in range(start_index, max_start_index + 1):
                    today_difficulty = max(today_difficulty, jobDifficulty[i])
                    dp[days_left][start_index] = min(
                        dp[days_left][start_index], today_difficulty + dp[days_left - 1][i + 1])
        return dp[d][0] if dp[d][0] < float('inf') else -1

    """
    Top-down Dynamic programming
    Time complexity: O((n - d)^2 * d)
    Space complexity: O((n - d) * d)
    """

    # def preprocess_hardest_job_remaining(self, jobDifficulty: List[int]) -> List[int]:
    #     n = len(jobDifficulty)
    #     hardest_job_remaining = [0] * n
    #     hardest_job = jobDifficulty[n-1]
    #     for i in range(n-1, -1, -1):
    #         hardest_job = max(jobDifficulty[i], hardest_job)
    #         hardest_job_remaining[i] = hardest_job
    #     return hardest_job_remaining

    # def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    #     # @lru_cache(None)
    #     def dp(start_index, d):
    #         if d == 1:
    #             return hardest_job_remaining[start_index]

    #         if (start_index, d) in memo:
    #             return memo[(start_index, d)]

    #         min_difficulty = float('inf')
    #         today_difficulty = 0
    #         num_jobs_left = n - start_index

    #         max_task_count = num_jobs_left - (d-1)
    #         for i in range(1, max_task_count + 1):
    #             today_difficulty = max(
    #                 today_difficulty, jobDifficulty[start_index + i - 1])
    #             # if today_difficulty > min_difficulty:
    #             #     break
    #             future_difficulty = dp(start_index + i, d - 1)
    #             difficulty = today_difficulty + future_difficulty
    #             min_difficulty = min(min_difficulty, difficulty)

    #         memo[(start_index, d)] = min_difficulty
    #         return min_difficulty

    #     n = len(jobDifficulty)

    #     if n < d:
    #         return -1

    #     hardest_job_remaining = self.preprocess_hardest_job_remaining(
    #         jobDifficulty)

    #     memo = {}
    #     return dp(0, d)


# @lc code=end
