def bubblesort(array):
    tamanhoArr = len(array)
    for i in range(0, tamanhoArr - 1):
        flag = False
        for j in range(0, tamanhoArr - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                flag = True
        tamanhoArr -= 1
        if not flag:
            break
    return array


lista = [10, 5, 3, 8, 1, 2]
print(bubblesort(lista))
