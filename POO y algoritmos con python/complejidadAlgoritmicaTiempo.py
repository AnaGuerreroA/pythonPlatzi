import time
import sys 

sys.setrecursionlimit(1500)

def factorial(n):
    respuesta = 1

    while n > 1 :
        respuesta *= n #esto es igual a respuesta =  respuesta * n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n -1)

if __name__ == "__main__":
    
    n = 1400
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    n = 1400
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)