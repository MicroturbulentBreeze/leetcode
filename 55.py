class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxn = 0
        l = len(nums)
        for i in range(l) :
            if i > maxn :
                break
            if i + nums[i] > maxn:
                maxn = i + nums[i]
        if maxn >= l-1:
            return True
        return False