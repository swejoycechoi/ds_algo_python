'''Non-recursive method for reversing a Python list.
'''
def reverse(sequence):
    S = ArrayStack()  # type: ignore # Create an empty stack
    # Step 1: Push all elements of the list onto the stack
    for j in range(len(sequence)):
        S.push(sequence[j])  # Add each element of the list to the stack

    # Step 2: Pop all elements from the stack and put them back in the list
    for j in range(len(sequence)):
        sequence[j] = S.pop()  # Take each element from the stack (in reverse order) and put it in the list