def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e: # ahora que conocemos el nombre del error podemos usarlo para manejar la excepcion
        print(e)
        return lista

lista =list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor)) #CON DIVISOR 2devuelve [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
                                                  #al dividir por 0 devuelve el error ZeroDivisionError: division by zero