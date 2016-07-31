import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def get_res(res,target,num_set,index,temp_set):
        	if target == 0:
        		res.append(copy.copy(temp_set))
        		return
        	for i in range(index,len(num_set)):
				if num_set[i]>target:
					return
				elif i>index and num_set[i]==num_set[i-1]:
					continue
				else:
					temp_set.append(num_set[i])
					get_res(res,target-num_set[i],num_set,i+1,temp_set)
					temp_set.pop()
        res=[]
        candidates.sort()
        get_res(res,target,candidates,0,[])
        return res