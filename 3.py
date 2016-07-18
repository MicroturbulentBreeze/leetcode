class Solution(object):
    def lengthOfLongestSubstring(self, a):
        """
        :type s: str
        :rtype: int
        """
        if a == "":
            return 0
        l = len(a)
        max_num = 1
        sum = 0
        last = 0
        first_flag = True
        d={}
        i=0
        while i < l:
        	if a[i] in d:
        		sum =i -last
        		if sum > max_num or first_flag:
        			max_num = sum
        			first_flag = False
        		i = d[a[i]]+1
        		last = i
        		d = {}
        	else :
        		d[a[i]] = i
        		i = i+1
        if  max_num < l - last:
        	max_num = l - last
        return max_num
        
        
        