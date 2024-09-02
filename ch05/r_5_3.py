import sys

# Create an empty list and define the number of operations
data = []
n = 100  # Feel free to adjust n based on how extensive you want the test to be

# Phase 1: Append elements to the list and observe size growth
print("Appending elements:")
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

# Phase 2: Pop elements from the list and observe if the size shrinks
print("\nPopping elements:")
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.pop()
