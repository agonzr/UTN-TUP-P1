# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
n = int(input("Por favor ingrese un número entero"))
print("El número",n,"tiene",len(str(n)),"digito(s)")

# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
n1 = int(input("Por favor ingrese un número"))
n2 = int(input("Por favor otro ingrese un número"))
suma = 0
for nros in range(n1 +1, n2):
    suma += nros
print("La suma de los números entre",n1,"y",n2,"es:",suma)

# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
STOP = 0
cont = 0
n = int(input("Por favor ingrese un número para comenzar: "))
while n != STOP:
    cont += n
    n = int(input("Ingrese el siguiente número o 0 (cero) para finalizar: "))
print("La suma total es:",cont)

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
print("Bienvenid a divina adivinador")
print("Adiviná el número entre 0 (creo) y 9 (nueve)")
print("Comencemos...")
guess = random.randint(0, 9)
i = 1
n = int(input("Ingresa el un número del 0 al 9: "))
if n < 0 or n > 9:
    while n != guess:
        i += 1
        n = int(input("Intentá de nuevo"))
    print("¡Correcto! El número era",guess,"Lo has logrado en",i,"intentos.")
else:
    print("Recordá ingresar solo números del 0 al 9")

# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for n in range(101 -1 -1):
    if n % 2 == 0:
        print(n)

# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
n1 = int(input("Por favor ingrese un número"))
suma = 0
if n1 > 0:
    for nros in range(0, n1 +1):
        suma += nros
    print("La suma de los números entre 0 y",n1, "es",suma)    
else:
    print("Recuerda debes ingresar un número entero positivo.")
    print("Programa Finalizado.")

# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
t_num = 100
par = 0
impar = 0
pos = 0
neg = 0
for i in range(t_num):
    n = int(input(f"Por favor ingrese el número {i + 1} de {t_num}: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    if n >= 0:
        pos += 1
    elif n < 0:
        neg += 1
print("La cantidad de números pares son",par)
print("La cantidad de números impares son",impar)
print("La cantidad de números positivos son",pos)
print("La cantidad de números negativos son",neg)

# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
import statistics 
t_num = 10
for i in range(t_num):
    n = int(input(f"Por favor ingrese el número {i + 1} de {t_num}: "))
print("La media de los números ingresados es:",statistics.mean([n]))

# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
n = int(input("Ingrese un número: "))
n_original = n
n_invertido = 0
while n > 0:
    digito = n % 10
    n_invertido = n_invertido * 10 + digito
    n //= 10
print(f"Número invertido de {n_original} es: {n_invertido}")