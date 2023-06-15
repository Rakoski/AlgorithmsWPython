def insertionsort(array):
    for passo in range(1, len(array)):
        numero_de_agora = array[passo]
        for j in range(passo - 1, -1, -1):
            if array[j] > numero_de_agora:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            else:
                array[j + 1] = numero_de_agora
                break
    return array


lista = [0, 4, 2, 6, 7, 8, 3, 5]
print(insertionsort(lista))