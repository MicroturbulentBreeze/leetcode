class Solution(object):
    def threeSumClosest(self, s, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s.sort()
        l = len(s)
        first_flag = True

        close = 0
        for i in range(l-2):
        	left = i+1
        	right = l-1
        	while left < right:
        		temp = target - s[i] - s[left] -s[right]
        		if first_flag or abs(close - target) > abs(temp):
        			close = target - temp
        			first_flag = False
        		if temp == 0:
        			return target
        		elif temp >0:
        			left = left +1
        		else:
        			right = right -1			
        	if i+1<l-2 and s[i+1]==s[i]:
        		i=i+1
        return close
		
s = [89,-13,38,-39,-58,32,9,97,-31,13,99,-100,-7,32,13,-32,-12,59,43,-62,89,-8,15,41,31,-48,-50,-80,-82,-22,-60,29,32,88,17,-76,10,4,55,4,65,83,-100,5,6,75,-13,4,57,-53,8,80,-79,-76,61,-52,100,74,-96,79,-72,-68,-56,-29,98,-52,-77,90,-48,21,78,-1,-6,8,19,69,-39,-74,-42,-39,-86,10,55,-84,-97,-79,76,84,-87,-49,-44,28,-88,-9,71,34,-72,85,9,-96,-4,-79,-52,95,20,-76,94,80,-38,-76,-70,-98,-19,34,-82,67,36,-98,74,-93,1,-92,-4,42,-26,-16,27,3,-61,41,66,-60,85,-21,-15,52,14,78,-80,60,-36,-35,-56,-76,-8,-25,56,-7,-8,-31,8,40,-25,-40,2,-44,7]
target = -71
print Solution().threeSumClosest(s,target)