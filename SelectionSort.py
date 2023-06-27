def selectionsort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista - 1):
        index_min = i
        for j in range(i + 1, tamanho_lista):
            if lista[j] < lista[index_min]:
                index_min = j
        temp = lista[i]
        lista[i] = lista[index_min]
        lista[index_min] = temp
    return lista


arr = [0, 4, 2, 6, 2, 7]
print(selectionsort(arr))

