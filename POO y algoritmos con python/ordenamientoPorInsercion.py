import  random

def lista_ordenada(lista):
    
    print(lista)
    #nueva_lista = lista[0:1]
    #tomar primer elemento de lista para nueva lista ordenada       
    #
    #
    #

    for i in range(1, len(lista)):
        valor_temporal = lista[i - 1]
       
        
    return print(lista)















    """

        valor_actual = nueva_lista[0:1]
        if  valor_actual < lista[i]:

            lista.remove(lista[0])
            contador = contador  + 1
            print(f'lista vuelta {contador }: {lista}')
            print(f'nueva lista vuelta {contador }: {nueva_lista}')
            nueva_lista.insert(0,lista[0])
            print(f'inserta {lista[0]}')
        
            
            print(nueva_lista)
            
            if nueva_lista[0] > nueva_lista[1]:
                nueva_lista[0], nueva_lista[1] = nueva_lista[1], nueva_lista[0]
                
                pass
    return nueva_lista 
"""

if __name__ == "__main__":
    rango_lista = 4#int(input('Inserta tamaño de la lista: '))
    lista = [49, 45, 63, 11]#[random.randint(0,100) for i in range(rango_lista)]
    lista_ordenada(lista)
    #print(lista)
    