def findlast(s,c):
	pos = -1
	i = -1
	for ch in s :
		pos +=1
		if ch == c:
			i=pos
	return i

def get_res(s):
	s1 = ['']
	for c in s:
		i = findlast(s1[-1],c)
		print c,s1,i,s1[-1][i+1:]
		if i<0:
			s1[-1]+=c
		else:
			s1.append(s1[-1][i+1:]+c)
	return max(map(len,s1))
	
s= "abcabcbb"
print get_res(s)