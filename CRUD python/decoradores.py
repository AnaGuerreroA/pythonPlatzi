def funcion_decoradora(funcion_a_decorar):
    def decorando():
        print('empezaremos una operacion')
        funcion_a_decorar()
        print('terminamos la operacion')
        print('*' *20)
    return decorando


@funcion_decoradora    
def funcion_suma():
    suma= 2+2
    print(suma)


@funcion_decoradora
def funcion_resta():
    resta= 3-2
    print(resta)

if __name__ == "__main__":
    funcion_suma()

    funcion_resta()