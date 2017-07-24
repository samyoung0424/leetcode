class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = []
        for i in range(len(nums)):
            dp.append(nums[i] + i)
        cur_max = 0
        for i in range(len(dp)):
            if cur_max < i:
                return False
            cur_max = max(cur_max, dp[i])
        return True
