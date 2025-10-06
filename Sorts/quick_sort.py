def quick_sort(lista):
    n = len(lista)

    if n <= 1:
        return lista
    else:
        pivote = lista[n//2]
        # Crear una nueva lista sin el pivote
        lista_sin_pivote = lista[:n//2] + lista[n//2+1:]
        menores = [i for i in lista_sin_pivote if i <= pivote]
        mayores = [i for i in lista_sin_pivote if i > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

lista = [3, 11, 6, 21, 9, 7, 10]

print(quick_sort(lista))