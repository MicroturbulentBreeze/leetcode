class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        a = str
        i=0
        flag = 1
        l = len(str)
        while i < l and str[i] ==' ':
        	i+=1
        if i < l and str[i] in ['+','-']:
        	flag = 2 * (str[i]=='+') - flag
        	i+=1
        while i < l and str[i] == '0':
        	i +=1
        if i == len(str):
        	return 0
        sum = 0
        for j in range(i,len(str)):
        	if str[j]>'9' or str[j] < '0':
        		break
        	sum = sum*10+(ord(str[j])-ord('0'))
        res = sum*flag
        if res > 2147483647 :
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res