my_list = [1, 2, 3]

print(my_list[0])

print(my_list[1:])

my_list.append(4)#append = añade// se añade valor 4

my_list[0] = True #python permite listas con valores de distintos tipos OTROS LENGUAJES NO PERMITEN ESTO
print(my_list)

print(my_list.pop()) #pop regresa un elemento [en este caso retorna 4] y al mismo tiempo lo elimina 
print(f'pop: {my_list}')


#las listas se pueden iterar

for element in my_list:
    print(element)

a = [1, 2, 3]
b = a   #B no es una copia distinta de B// B y A apuntan al mismo lugar en memoria.
print(id(a))
print(id(b))#ambos devuelven el mismo id, demostrando que apuntan al mismo objeto

c = [a, b]
print(c)
a.append(5) #se creería que modificamos solo A, pero al apuntar A y B al mismo objeto, ambas se modificaron
print(c)
