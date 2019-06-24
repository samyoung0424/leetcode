#
# @lc app=leetcode id=318 lang=python
#
# [318] Maximum Product of Word Lengths
#


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) < 2:
            return 0
        d = {}
        for i in range(len(words) - 1):
            if words[i] not in d:
                d[words[i]] = 0
                for j in range(i+1, len(words)):
                    hasCommonLetter = False
                    for c in words[j]:
                        if c in words[i]:
                            hasCommonLetter = True
                            break
                    if not hasCommonLetter:
                        d[words[i]] = max(len(words[j]), d[words[i]])
        res = 0
        for k, v in d.iteritems():
            res = max(res, len(k) * v)
        return res
