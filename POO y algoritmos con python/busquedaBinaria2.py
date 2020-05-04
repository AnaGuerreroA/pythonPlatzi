import random

def busqueda_lista(lista, objetivo, inicio, final):
    
    if  inicio > final:
        return False

    medio = (inicio + final)//2
    print(f'objetivo {objetivo} \ninicio :{inicio} final {final - 1}. valor en index {lista[medio]}')

   # print(f'Buscando {objetivo} entre {inicio} y {final}')
   
    if  objetivo == lista[medio]:
        return True
    elif objetivo > lista[medio]:
        return busqueda_lista(lista, objetivo, inicio, medio - 1)
    elif objetivo < lista[medio]:
        return busqueda_lista(lista, objetivo, medio + 1, final)



if __name__ == "__main__":
    largo_lista = 10
    objetivo = 101
    lista = sorted([random.randint(0,10) for i in range(largo_lista)])

    encontrado = busqueda_lista(lista, objetivo, 0, largo_lista)
    print(lista)
    print(f'El numero {objetivo} {"está" if encontrado else "no está"} en la lista')