import sys                          # provides getsizeof function
data = []							# start with an empty list	
n = 100

for k in range(n):					
	oldsize = sys.getsizeof(data)	# store the current size of the list in bytes
	data.append(None)                 	# increase the length of the list by one 
	if sys.getsizeof(data) != oldsize:	# check if the size in bytes have changed
		print("Capacity reach at", len(data)-1)	# print the index where the change ocurred
		oldsize = sys.getsizeof(data)	# update old size to the new size for the next iteration
