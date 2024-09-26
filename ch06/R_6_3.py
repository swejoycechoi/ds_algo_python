# solution 1
def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())

# solution 2
def transfer(S,T):
    while len(S) > 0:
        T.append(S.pop())