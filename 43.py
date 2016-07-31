a="123456"
b="234567"
res=[]

def muti_single(s1,s2):
	num1=ord(s2)-ord("0")
	r = 0
	res=[]
	print num1
	for i in range(len(s1)-1,-1,-1):
		#print s1[i]
		c=(ord(s1[i])-ord("0"))*num1+r
		r=c//10
		c=c%10
		
		res.append(c)
		#print r,c,res
	if r!=0:
		res.append(r)
	return res

length = len(b)
lengtha = len(a)
for i in range(length):
	temp = muti_single(a,b[i])
	temp = [0]*(length-i-1)+temp+[0]*(i+lengtha-len(temp)+2)
	res.append(temp)
	print len(temp)
print res
r = 0
res_str=""
for i in range(len(res[0])) :
	c = sum([ x[i] for x in res ])+r
	r = c//10
	print c%10
	res_str = str(c%10)+res_str
i=0
while res_str[i] == "0":
	i+=1
print res_str[i:]