#
# @lc app=leetcode id=475 lang=python
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (31.31%)
# Total Accepted:    44.7K
# Total Submissions: 142.6K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
#
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
#
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
#
# Note:
#
#
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
#
#
#
#
# Example 2:
#
#
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
#
#
#
#
#


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def findClosestHeaterDist(pos, heaters):
            l, r = 0, len(heaters) - 1
            while l <= r:
                m = (l + r) / 2
                if heaters[m] == pos:
                    return 0
                if heaters[m] < pos:
                    l = m + 1
                else:
                    r = m - 1
            l, r = min(l, len(heaters) - 1), max(0, r)
           # print l, r
            return min(abs(pos - heaters[l]), abs(heaters[r] - pos))
        curr_max = 0
        # This question is stupid!! Houses is not sorted wtf
        heaters = sorted(heaters)
        for h in houses:
            # print findClosestHeaterDist(h, heaters)
            curr_max = max(findClosestHeaterDist(h, heaters), curr_max)
        return curr_max
