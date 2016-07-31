

n = 5
res= "1"
while n > 1:
	i = 0
	ans = ""
	l = len(res)
	for j in range(1,l+1):
		#print i,j,ans
		if j == l:
			ans += str(j-i)+res[j-1]
		elif res[j]!=res[j-1]:
			ans += str(j-i)+res[j-1]
			i = j

	print ans
	res = ans
	n-=1