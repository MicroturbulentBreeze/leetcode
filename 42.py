class Solution(object):
    def trap(self, a):
        """
        :type height: List[int]
        :rtype: int
        """
        if a==[]:
            return 0
        def find_max(a):
        	index = [0]
        	max_num = a[0]
        	for i in range(1,len(a)):
        		if a[i]>max_num:
        			max_num=a[i]
        			index =[i]
        		elif a[i] == max_num:
        			index.append(i)
        	return max_num,index
        
        before = sum(a)
        max_num,index = find_max(a)
        l,r=0,0
        if len(index) == 1:
        	l=r=index[0]
        else:
        	l,r=index[0],index[-1]
        for i in range(l,r+1):
        	a[i]=max_num
        for i in range (1,l):
        	if a[i]<a[i-1]:
        		a[i]=a[i-1]
        for i in range(len(a)-2,r,-1):
        	if a[i]<a[i+1]:
        		a[i]=a[i+1]
        return sum(a)-before        