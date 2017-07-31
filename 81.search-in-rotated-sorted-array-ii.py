class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = len(nums)
        if l == 0:
            return False
        if l == 1:
            if nums[0] == target:
                return True
            else:
                return False

        mid = l/2 -1
        if nums[0] == nums[mid] and nums[mid] == nums[-1]:
            for item in nums:
                if item == target:
                    return True
            return False
        elif nums[mid] >= nums[0]:
            if nums[0] <= target <= nums[mid]:
                return self.search(nums[:mid+1], target)
            else:
                return self.search(nums[mid+1:], target)
        else:
            if nums[mid] <= target <= nums[-1]:
                return self.search(nums[mid:], target)
            else:
                return self.search(nums[:mid], target)

