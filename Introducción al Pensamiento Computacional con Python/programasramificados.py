"""
num_1 = int(input('Escoge un entero: '))
num_2 = int(input('Escoge otro entero: '))

if num_1 > num_2:
    print('El primer numero es mayor que el segundo')
elif num_1 < num_2:
    print('El segundo numero es mayor que el primero')
else:
    print('Los numero son iguales') 
"""
usuario_1 = input('Ingresa tu nombre: ')
edad_usuario_1 = int(input(f'{usuario_1} ingresa tu edad: '))
usuario_2 = input('Ingresa tu nombre: ')
edad_usuario_2 = int(input(f'{usuario_2} ingresa tu edad: '))

info_user_1 = f'{usuario_1} (edad {edad_usuario_1})'
info_user_2 = f'{usuario_2} (edad {edad_usuario_2})'

if edad_usuario_1 > edad_usuario_2:
    print(f'{info_user_1} es mayor que {info_user_2}')
elif edad_usuario_2 > edad_usuario_1:
    print(f'{info_user_2} es mayor que {info_user_1}')
else: 
    print(f'{info_user_1} y {info_user_2} tienen la misma edad')        


