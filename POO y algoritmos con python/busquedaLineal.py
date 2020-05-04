import random
def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        match = True
        break
    return match

if __name__ == "__main__":
    tamano_lista = (int(input('De que tamaño sera la lista? ')))
    objetivo = int(input('que numero quieres encontrar? '))

    lista = [random.randint(0,tamano_lista) for i in range(tamano_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    
    print(f'El  elemento {objetivo} {"Esta" if encontrado else "no esta"} en la lista')