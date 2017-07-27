class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] == 0:
                tmp =nums.pop(i)
                nums.insert(0, tmp)
                i += 1
            elif nums[i] == 2:
                tmp = nums.pop(i)
                nums.append(tmp)
            else:
                i += 1
            count += 1
        return
