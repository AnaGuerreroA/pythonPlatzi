#range(comienzo, fin, pasos)

my_range = range(1,5)
print(type(my_range)) #devuelve: <class 'range'>

for i in my_range: #devuelve del 1 al 4, no incluye el 5
    print(i)

my_range = range(0, 7, 2) #de 0 hasta 7 y vaya de 2 en 2
my_other_range = range(0, 8, 2)

print(my_range == my_other_range)#Value equality// devuelve TRUE

for i in my_range:
    print(f'i: {i}')

print('===============================')

for z in my_other_range:
    print(f'z: {z}')

print(id(my_range))    
print(id(my_other_range)) #nos enseña que no son el mismo objeto ya que tienen distinto id

my_other_range is my_range #object equality// compara si son el mismo objeto


for i in range(0, 101 ,2):
    print(i)

print('==========================================')

for i in range(1, 100,2):
    print(i)    
print('//////////////////////////////////////')    
for i in range(1,100,1):
    if(i % 2 != 0):
        print(i)
