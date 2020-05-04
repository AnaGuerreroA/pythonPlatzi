"""
#Argumentos de otras funciones
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(funcion, numeros):
    resultados = []
    for numero in numeros:
        resultado = funcion(numero)
        resultados.append(resultado)
        print(resultado)

nums = [1, 2, 3]
aplicar_operacion(multiplicar_por_dos, nums)
"""

"""
#Funciones en expresiones
#Una forma de definir una función en una expresión es utilizando el keyword
#lambda. lambda tiene la siguiente sintaxis: lambda <vars>: <expresion>.

sumar = lambda x, y: x + y

print(sumar(2, 3))
"""

#Funciones en estructuras de datos
def aplicar_operaciones(num):
    operaciones = [abs, float, abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-12.99999))
