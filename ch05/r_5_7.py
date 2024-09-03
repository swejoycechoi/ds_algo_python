def missing(A):
	found = [False] * len(A)    # Creates a list of False values with the same length 
	for val in A:               # Iterates over each value in the array A
		if found[val]:            # Check if the value has been seen before
			return val              # If it has, return it as the repeated number
		else:
			found[val] = True       # Mark the value as seen