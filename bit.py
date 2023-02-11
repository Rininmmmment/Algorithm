'''
bit全探索
---- example ----

'''
def Enumerate(A):
	SumList = []
	for i in range(2 ** len(A)):
		li = []
		for j in range(len(A)):
			wari = (2 ** j)
			if (i // wari) % 2 == 1:
				li.append(A[j])
		SumList.append(li)
	return SumList