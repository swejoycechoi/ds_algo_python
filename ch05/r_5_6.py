def insert(self, k, value):
    if self._n == self._capacity:  # Check if resizing is needed
        B = self._make_array(2 * self._capacity)  # Create a new array with double capacity
        
        # First loop: Copy elements before the insertion index k
        for j in range(k):
            B[j] = self._A[j]
        
        # Insert the new value directly at index k
        B[k] = value
        
        # Second loop: Copy the remaining elements after index k, shifted by one position
        for j in range(k, self._n):
            B[j + 1] = self._A[j]
        
        # Update the internal array to the new resized array
        self._capacity = 2 * self._capacity
        self._A = B
    else:
        # If no resizing is needed, just shift elements to the right as before
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
    
    self._n += 1  # Increment the size of the array
