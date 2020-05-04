import random
#meta: impleentar contador
def busqueda_binaria(lista, comienzo, final, objetivo, contador):
    print(f'Vuelta :{contador} \nBuscando {objetivo} entre elemento {comienzo} y elemento {final - 1}')

    if  comienzo > final:
        return False
    
    medio = (comienzo + final) // 2
    contador = contador + 1
    print(f'medio = {medio}')
    if  lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo: 
        return busqueda_binaria(lista, medio + 1, final, objetivo,contador)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1,  objetivo, contador)  

if __name__ == "__main__":
    tamano_lista = (int(input('De que tamaño sera la lista? ')))
    objetivo = int(input('que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)] )#sorted ordena la lista
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo,1)
    print(encontrado)
    print(lista)
    print(f'El  elemento {objetivo} {"Esta" if encontrado else "no esta"} en la lista ')