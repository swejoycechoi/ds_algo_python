# code fragment 5.3

from time import time
def comput_average(n):
	# perform n appends to an empty list and return average time elapsed
	data = []
	start = time()
	for k in range(n):
		data.append(None)
	end = time()
	return (end - start) /n
