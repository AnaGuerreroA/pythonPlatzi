clientes_diccionario = [
    {
        'nombre' : 'Ana',
        'trabajo' : 'programming'
    },
    {
        'nombre' : 'Aritza',
        'trabajo' : 'diseñadora'
    }
]

def print_clients(clients_):
    for indx, client in enumerate(clients_):
        print('{idx} | {nombre} | {trabajo}'.format(
            idx = indx,
            nombre = client['nombre'],
            trabajo = client['trabajo'],

        ))


if __name__ == "__main__":
    print_clients(clientes_diccionario)