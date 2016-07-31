class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        length = len(nums)
        for i in range(length):
            while nums[i]>0 and nums[i] <length and nums[i] != i+1 and nums[i] != nums[nums[i]-1]  :
                temp = nums[i]
                nums[i]=nums[temp-1]
                nums[temp-1]=temp
        for i in range(length):
            if i+1!=nums[i]:
                return i+1
        return length+1