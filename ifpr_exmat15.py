# Escreva o pseudocódigo de uma função iterativa e uma função recursiva para computar uma sequência
# S(n) dada por 5, 12, 19, 26, 33, ...

def itsequencia(num, tam=5):
    lista = []
    for c in range(tam):
        lista.append(num)
        num += 7
    return lista


print(itsequencia(5))


