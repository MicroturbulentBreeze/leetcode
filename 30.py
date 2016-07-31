class Solution(object):
    def findSubstring(self, a, b):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        l = len(b[0])
        n = len(a)/l
        b0 = set(b)
        d={}
        flag = 1
        step = 10
        while step < n:
        	step *=10
        for i in b0:
        	d[i] = flag
        	flag *=step
        list_a = []
        res = []
        right_ans = 0
        for i in b:
        	right_ans+=d[i]
        for i in range(0,len(a)-l+1):
        	num = d.get(a[i:i+l])
        	if num is None:
        		num = 0
        	list_a.append(num)	
        c=[0]*l
        res_len = l*len(b)
        for i in range(0,len(a)-l+1):
        	index = i%l
        	if i >=res_len:
        		c[index]=c[index] + list_a[i] - list_a[i-res_len]
        	else:
        		c[index]=c[index] + list_a[i]
        	if c[index] == right_ans:
        		res.append(i-res_len+l)		
        return res        