class Solution(object):
    def threeSumClosest(self, s, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s.sort()
        l = len(s)
        d = {}
        for i in range(l):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]]=[i]
        def get_close(left,right,temp):	
        	if left == right:
        		return s[left]
        	mid = left + (right-left)/2
        	if s[mid]==temp:
        		return s[mid]
        	elif s[mid]>temp:
        		return get_close(left,mid,temp)
        	else:
        		return get_close(mid+1,right,temp)
        res=0
        first_flag = True
        first_i_flag = False
        old_i = 0
        for i in range(l-2):
        	if first_i_flag and s[i] ==old_i:
        		continue
        	first_j_flag = False
        	old_j = 0		
        	for j in range (i+1,l-1):
        		if first_j_flag and s[j] ==old_j:
        			continue
        		temp=target - s[i] - s[j]
        		if temp in d:
        		    for k in d[temp]:
        		        if k > j:
        		            return target
        		close_n=get_close(j+1,l-1,temp) 
        		close_num = close_n+ s[i] +s[j]
        		if first_flag or abs(close_num-target) < abs(res-target):
        			first_flag = False
        			if close_num == target:
        			    return target
        			res=close_num
        		first_j_flag = True
        		old_j = s[j]		
        	first_i_flag = True
        	old_i = s[i]
        return res