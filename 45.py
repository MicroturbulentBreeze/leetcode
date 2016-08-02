class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length == 1:
            return 0
        l,r,jumps = 1,nums[0],1
        while r < length-1:
        	next_l = next_r = r+1
        	for i in range(l,r+1):
        		if i+nums[i] > next_r:
        			next_r=i+nums[i]
        	jumps += 1
        	l,r = next_l,next_r
        
        return jumps       