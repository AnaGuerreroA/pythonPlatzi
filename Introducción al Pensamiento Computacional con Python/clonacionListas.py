my_list = [1, 2, 3]


my_cloned_list = list(my_list)
#ambas tienen los mismos valores([1,2,3])
print(my_list)  
print(my_cloned_list)
#pero tienen distinto ID gracias a que añadimos "list()"
print(id(my_list))
print(id(my_cloned_list))
my_second_cloned_list = my_list[::] #[::]los puntos dobles(:) en este caso indican "desde el inicio" y "hasta el final"
#ambas tienen los mismos valores([1,2,3])
print(my_list)  
print(my_second_cloned_list)
#pero tienen distinto ID gracias a que añadimos "[::]" un rango de clonacion
print(id(my_cloned_list))
print(id(my_second_cloned_list)) 