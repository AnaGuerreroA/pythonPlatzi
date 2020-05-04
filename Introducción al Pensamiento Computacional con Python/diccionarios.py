my_dict = {
    'David' : 35,
    'Erika' : 32,
    'Jaime': 50,
}

print(my_dict['David'])

print(my_dict.get('Davi', 30)) #el metodo get nos devolvera 'davi' si es que existe y sino un 30. esto evita el error "KeyError:"

my_dict['Erika'] = 20 #asi podemos reasignar un valor
print(my_dict)
my_dict['Pedro'] = 70 #así podemos asignar nuevos valores

del my_dict['Jaime'] #asi podemos eliminar un valor
print(my_dict)

#iteraciones
for llave in my_dict.keys(): #devuelve los nombres/keys
    print(llave)

for valor in my_dict.values(): #devuelve las edades/valores
    print(valor)    

for llave, valor in my_dict.items(): #devuelve nombre y edad/ llave y valor
    print(llave, valor)    


print('David' in my_dict)# pregunta si david esta en mi diccionario. Si está devuelve true    