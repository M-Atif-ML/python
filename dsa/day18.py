class Solution(object):
    def findMaxLength(self, nums):
        diff_index = {0: -1}  # diff: first index where this diff occurred
        diff = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                diff += 1
            else:
                diff -= 1

            if diff in diff_index:
                max_len = max(max_len, i - diff_index[diff])
            else:
                diff_index[diff] = i

        return max_len


   