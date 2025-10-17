# La tupla es un tipo de dato que permite almacenar varios valores de diferente tipo
# Se añaden elementos en una tupla mediante paréntesis y separados por comas
# Las tuplas son inmutables, es decir, no se pueden modificar después de su creación
my_tupla = (53, 'perro', 7.4, True)
print(type(my_tupla))

# Igual que en las listas, podemos acceder a los elementos de una tupla utilizando índices, count...
print(my_tupla[1])
print(my_tupla.count(53))

# El .index() que va a encontrar el primer elemento que coincide con el valor buscado
print(my_tupla.index('perro'))

# Para pasar una tupla a una lista, podemos usar la función list()
my_tupla = list(my_tupla)
print(type(my_tupla))
# Para volver a una tupla, podemos usar la función tuple()
my_tupla = tuple(my_tupla)
print(type(my_tupla)) 

# Practica random
frutas_tupla = ('Manzana', 'Pera', 'Naranja', 'Kiwi', 'Sandia')
print(frutas_tupla)
print(type(frutas_tupla))

# Acceder a un elemento específico de la tupla
print(frutas_tupla[3])  # Kiwi
print(frutas_tupla[-1])  # Sandia

print(frutas_tupla.index('Pera'))  # Encontrar el índice de un elemento específico
print(len(frutas_tupla))  # Calcular la longitud de la tupla

# Convertir la tupla a una lista
frutas_tupla = list(frutas_tupla)
print(type(frutas_tupla))  