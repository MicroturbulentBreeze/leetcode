class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def myreverse(a,l,r):
        	length,m= l+r,l+(r-l)//2
        	for i in range(l,m+1):		
        		temp = a[i]
        		a[i] = a[length - i]
        		a[length - i] = temp      
        l= len(nums)
        if l==1:
            return
        for i in range(l-2,-1,-1):
            if nums[i] >=nums[i+1]:
                continue
            for j in range(l-1,-i,-1):
                if nums[i] >= nums[j]:
                    continue
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                
                myreverse(nums,i+1,l-1)
                return
        nums.reverse()
        print nums
        return 