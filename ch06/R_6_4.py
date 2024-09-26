'''Solution: If the stack is empty, then return (the stack is empty).
Otherwise, pop the top element from the stack and recur.
'''

def remove_all(S):
	# base case, if the stack is empty
	if len(S) == 0:
		print("the stack is empty")
		return
	else:
		#recursive case: pop top element and recursively call the function
		S.pop()
		remove_all(S)

# Example usage:
S = [1, 2, 3, 4, 5]  # Stack with 5 elements
remove_all(S)

print("S:", S)  # Should be an empty stack