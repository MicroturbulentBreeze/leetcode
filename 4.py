class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
    	"""
    	:type nums1: List[int]
    	:type nums2: List[int]
    	:rtype: float
    	"""		
    	m=len(nums1)
    	n=len(nums2)
    	flag = False
    	if (m+n)%2 == 0:
    		flag = True
    	if m == 0 and n == 0:
    		return 0
    	if n == 0:
    		if flag :
    			return (float)(nums1[m//2]+nums1[m//2-1])/2
    		else :
    			return nums1[m//2]
    	if m == 0:
    		if flag :
    			return (float)(nums2[n//2]+nums2[n//2-1])/2
    		else :
    			return nums2[n//2]
    	if m==1 and n==1:
    	    return (float)(nums1[0]+nums2[0])/2
    	l=0
    	r=m
    	i=0
    	res = 0
    	while l<=r:
    		i = (l + r)//2
    		
    		if flag :
    			j = (m+n-2*i)//2
    		else:
    			j = (m+n+1-2*i)//2
    		print l,r,i,j	
    		if j > n:
    			l+=1
    			continue 
    		if j < 0:
    			r -= 1
    			continue
    		if i == 0 :
    			if nums2[j-1] <= nums1[0]:
    				if flag :
    					if j!=n :
    						res = (float)(min(nums1[0],nums2[j]) + nums2[j-1])/2
    					else :
    						res = (float)(nums1[0] + nums2[j-1])/2
    				else :
    					res = nums2[j-1]
    				break
    			else :
    				l = i +1
    		elif j == 0 :
    			if nums2[0] >= nums1[i-1]:
    				if flag :
    					if i!=m :
    						res = (float)(min(nums2[0],nums1[i]) + nums1[i-1])/2		
    					else :
    						res = (float)(nums2[0] + nums1[i-1])/2		
    					
    				else :
    					res = nums1[i-1]			
    				break
    			else :
    				r = i -1
    		elif i == m and nums2[j] >= nums1[m-1]:
    			if flag :
    				res = (float)(nums2[j] + max(nums1[m-1],nums2[j-1]))/2		
    			else :
    				res = max(nums1[m-1],nums2[j-1])		
    			break	
    		elif j==n and nums2[n-1] <= nums1[i]:
    			if flag :
    				res = (float)(nums1[i] + max(nums1[i-1],nums2[n-1]))/2		
    			else :
    				res = max(nums1[i-1],nums2[n-1])		
    			break			
    		elif nums1[i] >= nums2[j-1] and nums2[j] >= nums1[i-1]:
    			if flag:
    				res = (float)(max(nums2[j-1],nums1[i-1])+min(nums1[i],nums2[j]))/2
    			else :
    				res = max(nums1[i-1],nums2[j-1])
    			break
    		elif nums1[i] < nums2[j-1]:
    			if l+1 == r:
    				l = r
    			else:
    				l = i
    		else:
    			if l+1 == r:
    				r = l
    			else:
    				r = i
    		print nums1[i] , nums2[j-1],l,r
    	return res
    	
    	
    	