import random
lista_de_numeros = list(range(100))

print(lista_de_numeros)

pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print('=' * 140)
print(pares)

student_uid = [1, 2, 3]
students = ['juan', 'jose', 'james']

students_with_uid = {uid: students for uid, students in zip(student_uid, students)}

print(students_with_uid)

#ZIP 
#If one tuple contains more items, these items are ignored:
# is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))

#FIN ZIP
print('*' * 100)
random_number = []

for i in range(10):
    random_number.append(random.randint(1,5))

print(random_number)

non_repited = {number for number in random_number}
print(non_repited) #set no admite repetidos asi que solo nos devolvera valores unicos