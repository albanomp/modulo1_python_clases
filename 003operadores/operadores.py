print(6 * 3) # Suma
print(6 - 3) # Resta
print(6 * 3) # Multiplicacion
print(11 / 3) # Division
print(9 % 3) # Modulo, residuo de la division
print(4 ** 3) # Exponente
print(11// 3) # Division de floors. Devuelve la parte entera de la division
redondeo_decimal = round(3.141592546,2) 
print(f"redondeo a 2 decimales: {redondeo_decimal}")


# Se puede hacer tambien con letras
print('Hola ' + 'Mundo')

# Tambien con numeros usando el string  
a = 6
print('Hola ' + str(a))

# Operadores de comparacion (Booleans)
print(6 > 3) # Mayor que
print(6 < 3) # Menor que
print(6 >= 3) # Mayor o igual que
print(6 <= 3) # Menor o igual que
print(6 == 3) # Igual que
print(6!= 3) # Diferente que 

# Operadores logicos

print(True and True) # and pregunta si ambos son true
print(True or False) # Con or solo pregunta si alguno de los dos es True
print(not True) # Not cambia el valor de True a False y viceversa

# Ejercicio de prueba
print((not(7 != 7)and 6 > 5)and('rozar' < 'rotar' or not(3 == 5))) 




print("\n")
print("=" * 20)
print("OPERADORES ARITMÉTICOS")
print("=" * 20)
print("\n")

precio_manzanas = 3
precio_naranjas = 5
total_frutas = precio_manzanas + precio_naranjas
print(f"Total de la compra: {total_frutas} euros")

dinero_entregado = 20
dinero_producto = 13
cambio = dinero_entregado - dinero_producto
print(f"Su cambio es: {cambio} euros")

precio_unitario = 5
cantidad = 3
precio_total = precio_unitario * cantidad
print(f"Precio por {cantidad} unidades: {precio_total} euros")

pizza = 8 / 2
print(f"8 / 2 = {pizza}")

horas_totales = 90
horas_por_dia = 24
dias_completos = horas_totales // horas_por_dia
print(f"Días completos: {dias_completos} días")

horas_restantes = horas_totales % horas_por_dia
print(f"Horas restantes: {horas_restantes} horas")

lado = 4
area = lado ** 2
print(f"El área del cuadrado es: {area} unidades cuadradas")

numero = 25
raiz_cuadrada = numero ** 0.5
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

numero = 27
raiz_cubica = numero ** (1/3)
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")

resultado = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultado}")

resultado_redondeado = round(resultado, 2)
print(f"Redondeado a 2 decimales: {resultado_redondeado}")

print("\n")
print("=" * 20)
print("OPERADORES DE COMPARACIÓN")
print("=" * 20)
print("\n")

precio_producto_a = 15
precio_producto_b = 10

es_mas_barato = precio_producto_b < precio_producto_a
print(f"¿El producto B es más barato que el A? {es_mas_barato}")

print("\n")
print("=" * 20)
print("OPERADORES LÓGICOS")
print("=" * 20)
print("\n")

ingresos_suficientes = True
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿Préstamo aprobado? {aprobacion_prestamo}")

ingresos_suficientes = False
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿Préstamo aprobado? {aprobacion_prestamo}")

es_socio = False
tiene_invitacion = True

puede_entrar = es_socio or tiene_invitacion
print(f"¿Puede entrar al evento? {puede_entrar}")

disponible = False
no_disponible = not disponible
print(f"¿El producto no está disponible?")

# EJERCICIO
print("=== CALCULADORA DE IMC ===\n")

# 1. Declara dos variables: 'peso' con valor 70 (en kilogramos) y 'altura' con valor 1.75 (en metros)
# Escribe aquí tu código para la variable peso
peso = 70

# Escribe aquí tu código para la variable altura
altura = 1.75 

print("=== DATOS INGRESADOS ===")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")

print("\n=== CÁLCULO DEL IMC ===")

# 2. Calcula el IMC utilizando la fórmula: peso / (altura ** 2)
# 3. Almacena el resultado en una variable llamada 'imc'
# Escribe aquí tu código

imc = peso / (altura ** 2)

# 4. Redondea el resultado a dos decimales usando la función round()
# Escribe aquí tu código
imc = round (imc,2)

print("=== RESULTADO ===")
# 5. Imprime el resultado con un mensaje descriptivo
# Escribe aquí tu código

print(f"Tu indice de masa corporal es: {imc}")