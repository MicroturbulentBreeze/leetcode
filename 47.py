import copy
class Solution(object):
    def permuteUnique(self, a):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a.sort()
        length = len(a)
        res = []
        def get_res(start,a,res,temp):
        	#print start,a,temp
        	if len(a) == 0: 
        		res.append(copy.copy(temp))
        		return 
        	s = copy.copy(a)
        	for i in range(len(s)):
        		if i!=0 and s[i] == s[i-1]:
        			continue
        		a.remove(s[i])
        		temp.append(s[i])
        		get_res(start+1,a,res,temp)
        		#print "==="
        		temp.pop()
        		a.insert(i,s[i])
        		#print temp
        temp = []
        get_res(0,a,res,temp)
        return res