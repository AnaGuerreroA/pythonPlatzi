import sys
import csv
import os

#clientes = ['Ana','Ailid','Aritza']#

##clientes_diccionario = [
##    {
##        'nombre' : 'Ana',
##        'trabajo' : 'Programador'
##    },
##    {
##        'nombre' : 'Ailid',
##        'trabajo' : 'Diseñadora'
##    },
##    {
##        'nombre' : 'Aritza',
##        'trabajo' : 'Diseñadora'
#    }
#]


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['nombre', 'compañia', 'email', 'posicion']
clientes_diccionario = []
clientes = []
def _initialize_client_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)
        for row in reader:
            clientes_diccionario.append(row)



def _save_clients_to_storage():
    with open(CLIENT_TABLE, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames= CLIENT_SCHEMA)
        writer.writerows(clientes_diccionario)
    print('pasó')


def _lista_clientes_diccionario():
    for idx, cliente in enumerate(clientes_diccionario):
        print('{idx}| {nombre} | {compañia} | {email} | {posicion}'.format(
            idx = idx,
            nombre = cliente['nombre'],
            compañia = cliente['compañia'],
            email = cliente['email'],
            posicion = cliente['posicion']
        ))


def _lista_clientes():
    for i in clientes:
        print('{nombre}'.format(
            nombre = i))


def _inserta_nuevo_cliente(nuevo_cliente):
    global clientes
    clientes.append(nuevo_cliente)
    return print(clientes)

def _inserta_datos_nuevo_cliente(nombre, compañia, email, posicion):
    global clientes_diccionario
    clientes_diccionario.append({'nombre': nombre, 'compañia': compañia, 'email':email, 'posicion':posicion})
    return _lista_clientes()


def _busca_cliente(cliente):
    global clientes
    enLista = False
    for cliente_lista in clientes:       
        if cliente_lista == cliente:
            enLista = True

    if enLista == True:
        print('El cliente se encuentra en la lista')
    else:
        print('El cliente NO está en la lista')


def _busca_cliente_diccionario(cliente):
    global clientes_diccionario
    enLista = False
    for idx, cliente_diccionario_b in enumerate(clientes_diccionario):
        if cliente_diccionario_b['nombre'] == cliente:
            enLista = True
    
    if enLista == True:
        print('El cliente si está en la lista')
    else:
        print('El cliente no esta en la lista')


def elimina_cliente(cliente):
    global clientes
    estaLista = False
    for cliente_lista in clientes:
        if  cliente_lista == cliente:
            clientes.remove(cliente)
            estaLista = True

    if estaLista == True:
        print('cliente eliminado correctamente')
    else:
        print('El cliente no se eliminó porque no está en la lista')


def elimina_cliente_diccionario(clientes):
    global clientes_diccionario
    estaLista = False

    for idx, cliente in enumerate(clientes_diccionario):

        if cliente['nombre'] == clientes:
            estaLista = True
            del clientes_diccionario[idx]

    if estaLista == True:
        print('Cliente eliminado correctamente')
    else:
        print('El cliente no esta en la lista')



if __name__ == "__main__":
    _initialize_client_from_storage()

    pregunta = None
    while pregunta == None:
        pregunta = input('¿Qué deseas hacer?\n[C]rear\n[B]uscar\n[E]liminar\n[L]istar\n').upper()
   

    if pregunta == "C":
        cliente = input('Inserte el nombre del nuevo cliente\n')
        _inserta_nuevo_cliente(cliente)
    
    elif pregunta == "CD":
        cliente_nombre = input('Inserte el nombre del nuevo cliente\n')
        cliente_compañia = input('Inserte la compañia del nuevo cliente\n')
        cliente_email = input('Inserte el correo del nuevo cliente\n')
        cliente_posicion = input('Inserte la posicion de trabajo del nuevo cliente\n')
        _inserta_datos_nuevo_cliente(cliente_nombre,cliente_compañia,cliente_email,cliente_posicion)

    elif pregunta == "B":
        cliente = input('Inserte el nombre del cliente que desea buscar\n')
        _busca_cliente(cliente)
       

    elif pregunta == "BD":
        cliente = input('Inserte el nobre del cliente que desea buscar\n')
        _busca_cliente_diccionario(cliente)

    elif pregunta == 'L':
        _lista_clientes()

    elif pregunta == "LD":
        _lista_clientes_diccionario()
    
    elif pregunta == "E":
        cliente= input('Ingrese el nombre del cliente a eliminar\n')
        elimina_cliente(cliente)
        _lista_clientes()
        
    elif pregunta == "ED":
        cliente= input('Ingrese el nombre del cliente a eliminar\n')
        elimina_cliente_diccionario(cliente)
        _lista_clientes_diccionario()
    
    _save_clients_to_storage()