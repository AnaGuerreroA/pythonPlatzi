import sys
import csv
import os


CLIENT_TABLE = 'CRUD python/.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_client_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames = CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)



def _save_clients_to_storage():
#    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
#    with open(tmp_table_name, mode='w') as f:      
#        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
#        writer.writerows(clients)
#        os.remove(CLIENT_TABLE)        
#        os.rename(tmp_table_name, '.clients.csv')
    with open(CLIENT_TABLE, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames= CLIENT_SCHEMA)
        writer.writerows(clients)
    print('pasó')


def create_client(clien_data):
    global clients
    
    clients.append(clients)


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {position}'.format(
            uid=idx,
            name= client['name'],
            company=client['company'],
            email =client['email'],
            position = client['position'],
        )) 


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client not in client\'s list')


def search_client(client_name):
   
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('what is the client{}'.format(field_name))
    return field
    

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _initialize_client_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        clients = {            
            'name':_get_client_field(' name\n'),
            'company':_get_client_field(' company\n'),
            'email':_get_client_field(' email\n'),
            'position':_get_client_field(' position\n')
        }
        create_client(clients)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the new client name? ')

        update_client(client_name, updated_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')


    _save_clients_to_storage()
