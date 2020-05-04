def f(x):
    respuesta = 0

    for i in range(1000):
        respuesta += 1
       
    print(respuesta)

    for i in range(x):
        respuesta += x

    print(respuesta)

    for i in range(x):
        for j in range(x):
              respuesta += 1
              respuesta += 1

    print(respuesta)

if __name__ == "__main__":
   
    print(f(100))