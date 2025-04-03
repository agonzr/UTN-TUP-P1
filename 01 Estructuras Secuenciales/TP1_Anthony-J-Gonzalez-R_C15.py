# Crear un programa que imprima por pantalla el mensaje: Hola Mundo!.
print("¡Hola Mundo!")

# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("¡Hola Hola!")
name = input("Bienvenido(a), por favor escribe tu nombre: ")
print(f"¡Hola {name}!")

# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
print("Bienvenido, para iniciar el programa te pediré algunos datos")
name = input("Escribe tu Nombre: ")
last_name = input("Ahora, escribe tu Apellido: ")
age = input("¿Cual es tu edad? ")
address = input("Por ultimo, dinos tu lugar de Residencia: ")
print(f"Soy {name} {last_name}, tengo {age} años y vivo en {address}.")

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("Bienvenido, hoy te ayduaré a calcular el área y perímetro de un radio")
r = input("Por favor ingresa el valor del radio: ")
r = int(r)
pi = 3.1416
A = pi * (r**2)
P = (2 * pi) * r
print(f"El Area(A) del circulo es: {A} y su perimetro(P) es: {P}")

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
print("Hola Hola, hoy vamos a calcular la cantidad de horas")
seg = input("Ingresa la cantida de segundos")
seg = int(seg)
hrs = seg / 3600
hrs = round(hrs, 1)
print(f"{seg} equivalen a {hrs} horas.")

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("Bienvenido, el día de hoy aprenderemos la tabla del multiplicar")
num = input("Ingresa el número que desees ver la tabla de multiplizar: ")
num = int(num)
print(f"¡Genial! Aca tenes la tabla del {num}:")
print(f"{num} X 1 = {num * 1}")
print(f"{num} X 2 = {num * 2}")
print(f"{num} X 3 = {num * 3}")
print(f"{num} X 4 = {num * 4}")
print(f"{num} X 5 = {num * 5}")
print(f"{num} X 6 = {num * 6}")
print(f"{num} X 7 = {num * 7}")
print(f"{num} X 8 = {num * 8}")
print(f"{num} X 9 = {num * 9}")
print(f"{num} X 10 = {num * 10}")

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
n1 = input("Por favor ingresa un núermo distinto a 0 (cero): ")
n2 = input("Ahora ingresa otro núermo distinto a 0 (cero): ")
n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2
print(f"La Suma de {n1} + {n2} es: {suma}")
print(f"La Resta de {n1} - {n2} es: {resta}")
print(f"La Multiplicación de {n1} X {n2} es: {multi}")
print(f"La División de {n1} / {n2} es: {divi}")

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en Kg / (altura en m)2
print("¡Hola Hola! Para calcular tu Indice de Masa Corporal (IMC) te voy a pedir unos datos:")
alt = input("Por favor ingresa tu altura en centimetros (cm): ")
peso = input("Ahora ingresa tu peso en kilogramos (kg): ")
alt = float(alt)
peso = float(peso)
icm = peso / (alt ** 2)
icm = float(icm)
icm = round(icm, 1)
print(f"Con la altura {alt} y tu peso de {peso} tu ICM es de: {icm}")

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
# Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 X 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
print("Bienvenido a la convertidor de grados Celsius a Fahrenheit")
c = input("Ingrese la temperatura que desea convertira Fahrenheit F°: ")
c = float(c)
f = (c * 9/5) + 32
f = float(f)
f = round(f, 1)
print(f"La temperatura {c} en F° es: {f}")

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("¡Hola! Para calcular el promedio te pediré 3 números")
n1 = input("Ingresa el primero número: ")
n2 = input("Ingresa el segundo número: ")
n3 = input("Ingresa el último número: ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio}.")