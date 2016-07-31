
def get_res(l,r,nums,target):
	if l == r :
		return l if nums[l] == target else -1
	if l+1 == r:
		if nums[r] == target :
			return r
		return l if nums[l] == target else -1
	m = l + (r-l)/2
	i=get_res(l,m,nums,target)
	if i != -1:
		return i
	else:
		return get_res(m+1,r,nums,target)

a=[4,5,6, 7, 0, 1, 2]
print get_res(0,len(a)-1,a,2)