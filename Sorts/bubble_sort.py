def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range (0, n-1-i):
            if lista[j]>lista[j+1]:
                lista [j], lista [j+1] = lista[j+1], lista [j]
    return lista

lista = [3, 11, 6, 21, 9, 7, 10]

print(bubble_sort(lista))