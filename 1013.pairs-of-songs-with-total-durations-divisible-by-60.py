#
# @lc app=leetcode id=1013 lang=python
#
# [1013] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (42.62%)
# Total Accepted:    5.2K
# Total Submissions: 12.3K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
#
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i < j with
# (time[i] + time[j]) % 60 == 0.
#
#
#
# Example 1:
#
#
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
#
#
#
# Example 2:
#
#
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
#
#
#
#
#
# Note:
#
#
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
#
#
#

import collections


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        cnt = 0
        cnt_dist = {}
        for t in time:
            if t % 60 not in cnt_dist:
                cnt_dist[t % 60] = 1
            else:
                cnt_dist[t % 60] += 1
        for t in time:
            if (60 - t % 60) in cnt_dist or t % 60 == 0:
                if (t % 60) != 30 and t % 60 != 0:
                    cnt += cnt_dist[60 - t % 60]
                else:
                    cnt += cnt_dist[t % 60] - 1
        return cnt/2
