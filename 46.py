import copy
class Solution(object):
    def permute(self, a):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(a)
        res = []
        def get_res(a,res,temp):
        	if len(a) == 0:
        		res.append(copy.copy(temp))
        		return
        	for i in copy.copy(a):
        		a.remove(i)
        		temp.append(i)
        		get_res(a,res,temp)
        		temp.pop()
        		a.add(i)
        temp = []
        get_res(set(a),res,temp)        
        return res