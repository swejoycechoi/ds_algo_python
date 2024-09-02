# the code ran in my computer
import sys
data = []
n = 30        # you can set n to any value
for k in range(n):
	a = len(data)
	b = sys.getsizeof(data)
	print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
	data.append(None)