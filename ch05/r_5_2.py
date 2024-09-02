"""
import sys                           # provides getsizeof function

data = [ ]

for k in range(n):
	oldsize = sys.getsizeof(data)
	data.append(None)                  # increase length by one
	if sys.getsizeof(data) != oldsize:
		#print("Capacity reached at", len(data) − 1)
	oldsize = sys.getsizeof(data)
"""