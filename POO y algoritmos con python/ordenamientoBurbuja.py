import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n): # O(n)
        for j in range(0, n - i - 1):#O(n- i -  1) pero solo importa el numero mas grande : O(n)
                                        #esto da O(n * n ) que es igual a O(n**2) big o de n al cuadrado
            if lista[j] > lista[j + 1]:
                """
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
                """
                lista[j], lista[j+1] = lista[j+1], lista[j] 

    return(lista)
if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamaño sera la lista '))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)