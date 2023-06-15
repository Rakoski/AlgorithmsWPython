def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)
    # recursive function


def itfatorial(n):
    temp = 1
    for c in range(1, n+1):
        temp *= c
    return temp


print(itfatorial(6))
