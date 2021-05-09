def merge(a,b):
# merging two sorted lists
	merged = []
	i = 0
	j = 0
	while (i<len(a)) or (j<len(b)):
		if i == len(a):
			merged.append(b[j])
			j += 1
		elif j == len(b):
			merged.append(a[i])
			i += 1
		else:
			if a[i] <= b[j]:
				merged.append(a[i])
				i += 1
			else:
				merged.append(b[j])
				j += 1
	return merged

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = len(arr) // 2
		L = merge_sort(arr[:mid])
		R = merge_sort(arr[mid:])
		return merge(L, R)