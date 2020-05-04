#LAS TUPLAS SON INMUTABLES: NO PUEDEN SER MODIFICADAS
#LAS TUPLAS SON ASIGNABLES: PODEMOS ASIGNARLAS A DIFERENTES VARIABLES


my_tuple = ()
print(type(my_tuple)) # retorna <class 'tuple'> porque es una tupla
my_tuple = (1, 'dos', True)
print(my_tuple[0])

#my_tuple[0] = 2 Dará error porque no se pueden modificar los valores de una tupla

my_tuple = (1)
print(type(my_tuple)) #retorna <class 'int'> porque para definir una tupla necesitamos separar por comas(,)
my_tuple = (1,)
print(type(my_tuple)) #retorna <class 'tuple'> 


my_other_tuple = (2,3,4)
my_tuple += my_other_tuple #esto NO da error porque no es modificar los valores, es REASIGNAR valores y eso si está permitido
print(my_tuple)


x, y, z = my_other_tuple

print(f'x = {x} \nz = {z} \ny = {y}')

def coordenadas():
    return(5, 4)

coordenada = coordenadas()    
print(coordenada)
x, y = coordenadas()
print(x, y)