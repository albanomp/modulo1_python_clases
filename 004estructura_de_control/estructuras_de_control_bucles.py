print("\n")
print("=" * 20)
print("ESTRUCTURAS CONTROL ITERATIVO")
print("=" * 20)
print("\n")

print("\n")
print("=" * 20)
print("BUCLES FOR")
print("=" * 20)
print("\n")

frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

for fruta in frutas:
    print(fruta)

print("\n")
print("=" * 20)
print("RANGE")
print("=" * 20)
print("\n")

for i in range(5):
    print(i)
    
print("\n")

for i in range(3, 8):
    print(i)
    
print("\n")

for i in range (2, 11, 2):
    print(i)
    
print("\n")

for i in range(5, 0, 1):
    print(i)
    
print("\n")

# cuenta atrás hasta 0
for i in range(5, -1, -1):
    print(i)

print("\n")
print("=" * 20)
print("ITERAR SOBRE ÍNDICES")
print("=" * 20)
print("\n")

nombres = ["Ana", "Carlos", "Elena"]
print(f"Lista de nombres: {nombres}")

for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

print("\n")

for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

print("\n")
print("=" * 20)
print("BUCLES WHILE")
print("=" * 20)
print("\n")


"""

Bucle while

Bucle indeterminado, porque se ejecuta en base a condiciones por lo que 
a priori podemos no saber cuántas veces se va a ejecutar.

Ideal para crear aplicaciones de consola (CLI apps)

"""

# Bucles infinitos controlados
# Un bucle infinito es aquel que, en principio, no tiene una condición de salida natural.
# Se implementa con while True: y generalmente incluye una condición de salida explícita usando break:

while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()
    
    if respuesta == "n":
        print("Programa finalizado.")
        break
    
    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")
        
        
# La sentencia break
# La instrucción break permite terminar inmediatamente un bucle, saltándose todas las iteraciones restantes. 
# Cuando Python encuentra un break, sale del bucle más interno que lo contiene y continúa con el código que sigue después del bucle.

#Imagina break como un "botón de emergencia" que te permite escapar de un bucle 
# cuando se cumple cierta condición:

for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")

# La sentencia continue
# Mientras que break termina todo el bucle, continue salta únicamente la iteración actual 
# y pasa a la siguiente. Es como decir "ignora el resto de esta vuelta y continúa con la siguiente".

for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración
    
    print(f"Número impar: {numero}")
    
    
    
# Ejercicio bucles

# Solicitar al usuario la altura del triángulo
altura = input("Introduce la altura de un triángulo: ")

# Convertir la entrada a número entero
altura = int(altura)

print(f"\nGenerando patrón triangular de altura {altura}:")
print("-" * 30)

# Generar el patrón usando bucles for anidados
# Bucle externo: para cada fila (desde 1 hasta la altura)
for i in range(1, altura + 1):

    # Bucle interno: para cada número en la fila actual (desde 1 hasta el número de fila)
    for j in range(1, i + 1):

        # Imprimir cada número seguido de un espacio (sin salto de línea)
        print(j, end=" ")

    # Después de completar una fila, hacer un salto de línea
    print()

print("-" * 30)
print("Patrón completado!")
