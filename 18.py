# -*- coding : utf-8 -*-
class Solution(object):
    def fourSum(self, s, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s.sort()
        l = len (s)
        
        d = {}
        for i in range(l):
        	if s[i] in d:
        		d[s[i]].append(i)
        	else:
        		d[s[i]] = [i]
        
        res = []
        last_i = 1+target
        not_first_i= False
        for i in range (l):
        	if  not_first_i and s[i]==last_i:
        		continue
        
        	target1 = target - s[i]
        	last_j=target1+1
        	not_first_j= False
        	for j in range (i+1,l):
        		if not_first_j and s[j] == last_j:
        			continue
        		
        		target2 = target1 - s[j]
        		last_k = target2+1
        		not_first_k= False
        		for k in range(j+1,l):
        			if not_first_k and s[k] == last_k:
        				continue
        			target3 = target2 - s[k]
        			#print target1,target2,target3
        			if target3 < s[k]:
        				break
        			elif target3 in d :	
        				if target3 > s[k]:  
        					res.append ([s[i],s[j],s[k],target3])
        				else:
        					n = 1
        					for m in [s[i],s[j],s[k]]:
        						if m == target3:
        							n=n+1
        					if n <= len(d[target3]):
        						res.append ([s[i],s[j],s[k],target3])
        			last_k = s[k]
        			not_first_k = True
        		last_j = s[j]
        		not_first_j = True
        	last_i = s[i]
        	not_first_i = True
        return  res 