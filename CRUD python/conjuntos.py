a = (1,1,1,1,1,1,2,3,4,5,6,7,8)
print(type(a)) #<class 'tuple'>

print(a.count(1)) #cuenta cuantos 1 hay en la tupla
print(a.index(1)) #retorna el primer index de 1 que encientre

a = set([1,2,3])
print(type(a)) #<class 'set'>

b = {3,4,5}
print(type(b)) #<class 'set'>

a.add(3)
print(a) #no se modificó porque los set no pueden tener duplicados

a.add(20)
print(a) #ahora si se modifica porque es un valor que antes no estaba

print(a.intersection(b)) #muestra los elementos repetidos entre ambos, en este caso '{3}'
print(a.union(b)) #todos los elementos sin duplicados, en este caso '{1, 2, 3, 20, 4, 5}'
print(a.difference(b)) #todos elementos en A que no estan en B, en este caso: '{1, 2, 20}' 
print(b.difference(a)) #todos elementos en B que no estan en A, en este caso: '{4, 5}'

a.remove(20) #elimina
print(a)

print(dir(a))