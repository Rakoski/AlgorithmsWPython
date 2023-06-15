import math

def seqexptres(tam=5):
    lista = []
    for c in range(tam):
        num = c
        lista.append(math.pow(3, num))
    return lista


print(seqexptres(10))
