import math

vetor = [1, 2, 4, 5, 9, 14, 17, 21, 22, 24]
target = 17


def binarySearch(lista, target):
    meio = math.floor((len(lista) - 1) / 2)
    for i in range(len(lista)):
        if lista[i] < lista[meio]:
            if lista[i] == target:
                return lista[i]
        elif lista[i] > lista[meio]:
            if lista[i] == target:
                return lista[i]
        elif lista[meio] == target:
            return lista[meio]
    return -1


print(binarySearch(vetor, target))
