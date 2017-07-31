class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, i = 0, 0
        mv_cnt = 0
        while count < len(nums):
            if i < len(nums) - 2:
                if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                    nums.pop(i)
                    nums.append(i)
                    mv_cnt += 1
                else:
                    i += 1
                count += 1
            else:
                count += 1

        if len(nums) == mv_cnt:
            return min(2, mv_cnt)
        else:
            return len(nums) - mv_cnt
