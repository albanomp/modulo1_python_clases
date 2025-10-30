"""En Python, los errores durante la ejecución de un programa se denominan excepciones. Cuando ocurre un error, el programa normalmente se detiene y muestra un mensaje de error. Sin embargo, en muchas situaciones, queremos que nuestro programa continúe funcionando incluso cuando se produce un error. Aquí es donde entra en juego el manejo de excepciones mediante la estructura try-except."""

# Ejemplo 1 con ZeroDivisionError "en operaciones matematicas"
try:
    resultado = 10/0
except ZeroDivisionError:
    print(f"No se puede dividir por 0")
    

# Excepciones con tipo de datos: 
# TypeError: Se produce cuando una operación o función se aplica a un objeto de tipo inapropiado.
try:
    resultado = "42" + 10  # Intentar sumar un string y un entero
except TypeError:
    print("No se pueden sumar tipos diferentes")


# ValueError: Ocurre cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado.
try:
    numero = int("abc")  # Intentar convertir una cadena no numérica a entero
except ValueError:
    print("La cadena no representa un número válido")
    
# Excepciones relacionadas con índices y clavesCuando trabajamos con estructuras de datos como listas o diccionarios:

# IndexError: Se produce al intentar acceder a un índice que está fuera del rango de una secuencia.
try:
    lista = [1, 2, 3]
    elemento = lista[10]  # Intentar acceder a un índice que no existe
except IndexError:
    print("El índice está fuera del rango de la lista")


# KeyError: Ocurre cuando intentamos acceder a una clave que no existe en un diccionario.
try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]  # Intentar acceder a una clave inexistente
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")
    
# NameError: Ocurre cuando intentamos usar una variable o nombre que no está definido.
try:
    print(numero45)  # Intentar usar una variable que no existe
except NameError:
    print("La variable no está definida")
    
"""La cláusula else
La cláusula else en un bloque try-except se ejecuta únicamente cuando no ocurre ninguna excepción en el bloque try. Podemos pensar en ella como el código que se ejecuta cuando todo sale bien."""

try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"El resultado es: {resultado}")
    # Este código solo se ejecuta si no hubo excepciones

# En este ejemplo, el mensaje con el resultado solo se mostrará si la conversión a entero y la división se realizan correctamente, sin generar ninguna excepción.

 # La cláusula else resulta especialmente útil para separar el código que podría fallar del código que depende de su éxito. Esto hace que nuestro programa sea más claro y fácil de mantener.
 
"""La cláusula finally
La cláusula finally contiene código que se ejecuta siempre, independientemente de si ocurrió una excepción o no. Es ideal para tareas de limpieza que deben realizarse en cualquier caso, como cerrar archivos o conexiones."""

try:
    archivo = open("registro.txt", "w")
    archivo.write("Operación iniciada\n")
    # Código que podría generar una excepción
    resultado = 10 / int(input("Introduce un número: "))
    archivo.write(f"Resultado: {resultado}\n")
except ZeroDivisionError:
    archivo.write("Error: División por cero\n")
except ValueError:
    archivo.write("Error: Valor no válido\n")
finally:
    archivo.write("Operación finalizada\n")
    archivo.close()  # El archivo se cierra siempre
    print("Proceso completado")

# En este ejemplo, independientemente de si la operación tiene éxito o genera una excepción, el archivo se cerrará correctamente y se mostrará el mensaje "Proceso completado".

    """
    La cláusula "finally" es útil para: liberar recursos; restaurar datos; registrar finalizacion
    
    """

# Orden de ejecución
"""Es importante entender el orden de ejecución de estas cláusulas:

El código en el bloque try se ejecuta primero
Si ocurre una excepción, se ejecuta el bloque except correspondiente
Si no ocurre ninguna excepción, se ejecuta el bloque else
El bloque finally se ejecuta siempre, al final"""

def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
        # Descomentar para generar una excepción:
        # x = 1 / 0
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")
    
    print("5. Continuando después del bloque try")

demostrar_orden()