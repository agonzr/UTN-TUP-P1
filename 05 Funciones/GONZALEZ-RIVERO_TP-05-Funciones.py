# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo ():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario (nombre):
    return f"Hola {nombre}!"

nombre = input("Por favor ingresá tu nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("¿Cúal es tu nombre? ")
apellido = input("¿Cúal es tu apellido? ")
edad = int(input("¿Cuantos años tenés? "))
residencia = input("¿En que zona vivis? ")

informacion_personal(nombre, apellido, edad, residencia)

# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi

def calcular_area_circulo(radio):
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = float(input("Por favor ingresá el radio del círculo: "))
A = calcular_area_circulo(radio)
P = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {A:.2f}")
print(f"El perímetro del círculo es: {P:.2f}")

# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá la cantidad de segundos para convertirlos a horas: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.
# Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
    
numero = int(input("Ingresá el número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    divi = a / b if b != 0 else "Indefinido"
    return suma, resta, multi, divi

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))
suma, resta, multi, divi = operaciones_basicas(a, b)

print(f"La suma de {a} + {b} es = {suma}.\nLa resta de {a} - {b} es = {resta}.\nLa multiplicación de {a} x {b} es = {multi}.\nLa división de {a} / {b} es = {divi}.")

# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Por favor ingrese su peso en kilogramos: "))
altura = float(input("Ahora ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su Indice de masa corporal (IMC) es: {imc:.2f}.")

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Grados Celsius a convertir en Fahrenheit: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el último número para conocer el promedio: "))
promedio = calcular_promedio(a, b, c)

print(f"El promedio de los tres números ingresados es: {promedio:.2f}.")