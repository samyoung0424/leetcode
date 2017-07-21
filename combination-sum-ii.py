class Solution(object):
    def dfs(self, nums, target, cur_sol, res):
        if target == 0 :
            res.append(cur_sol)
            return
        if target < 0:
            return
        for i in range(len(nums)):
            if i==0 or nums[i] != nums[i-1]:
                self.dfs(nums[i+1:], target-nums[i], cur_sol+[nums[i]], res)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res

