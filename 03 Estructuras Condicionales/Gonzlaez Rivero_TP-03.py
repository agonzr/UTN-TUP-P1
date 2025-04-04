# 1. Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
print("¡Con este programa verificaremos su edad!")

# Solicitamos la edad al usuario.
age = int(input("Ingrese su edad: "))

# Definimos 18 años como mayoria de edad.
OLD = 18

# Evaluamos la condición y mostramos el mensaje.
if age >= OLD:
    print("¡Es mayor de edad!")
else:
    print("¡Lo siento! Aun no es mayor de edad")


# 2. Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
print("¡Aca podes verificar si estas aprobado!")

# Solicitamos al usuario la nota.
score = int(input("Ingrese su nota: "))

# Evaluamos la condición de aprobación y mostramos el mensaje.
if score >= 6:
    print("¡Aprobado!")
else:
    print("¡Desaprobado")


# 3. Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

# Solicitamos el valor al usuario
n_even = int(input("Por favor ingrese un número par para continuar: "))

# Evaluamos la condición usando el operador de modulo (%) y ostramos el mensaje.
if n_even % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

# Definimos las edades por categoría.
CHILD = 12
TEEN = 18
ADULT = 30

# Solicitamos el valor de la edad.
print("Verifiquemos juntos a que categoria pertenece")
cat = int(input("Por favor ingrese su edad actual: "))

# Evaluamos si las condiciones de edad por categoría se cumplen.
if cat <= 0: # Verificamos ingrese la edad en numeros positivos y mayor que 0, para esta verificación es mejor usar while.
    print("Por favor ingrese un número distinto ó mayor que 0 (cero)")
elif cat < CHILD:
    print("Peteneces a la categoría Niño/a")
elif cat >= CHILD and cat < TEEN:
    print("Perteneces a la categoria Adolescente")
elif cat >= TEEN and cat < ADULT:
    print("Perteneces a la categoria Adulto/a Joven")
elif cat >= ADULT:
    print("Perteneces a la categoria Adulto/a")


# 5. Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
print("Para crear una contraseña segura asegurate tenga entre 8 a 14 carácteres")
print("Verifiquemos juntos")

# Solicitamos al usuario su contraseña
password = input("Por favor ingresa una contraseña: ")

# Definimos y calculamos la longitud de la contraseña con la funcion len()
length = len(password)

# Evaluamos si la contraseña cumple los parametros y mostramos el mensaje.
if length >= 8 and length <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6. Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Importamos los modulos/librerias que necesitamos
from statistics import mode, median, mean
import random

# Creamos la listas de numeros aleatorios
n_random = [random.randint(1, 100) for i in range(50)]

# Definimos y calculamos la moda, mediana y media usando el random
moda = mode(n_random)
mediana = median(n_random)
media = mean(n_random)

# Evaluamos si se cumple las condiciones de Sesgo positivo, negativo o sin riesgo.
if media > mediana > moda:
    print("¡El sesgo es positivo!")
    print(f"El valor de la media es {media} mayor que la mediana {mediana} y, a su vez, la mediana es mayor que la moda {moda}")
elif media < mediana < moda:
    print("¡El sesgo es Negativo!")
    print(f"El valor de la media es {media} menor que la mediana {mediana} y, a su vez, la mediana es menor que la moda {moda}")
elif media == mediana == moda:
    print("¡Sin riesgo!")
    print(f"El valor de la media es {media} igual que la mediana {mediana} y que la moda {moda}")
else:
    print("Error en los datos")


#7. Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
print("¡Verifiquemos las vocales!")

# Solicitamos al usuario la palabra.
word = input("Ingresa una palabra: ")

# Recorremos el string para ver cuantos digitos tiene
length = len(word)
l_letter = word[length - 1]  # Obtenemos el último carácter

# Evaluamos si la condición se cumple (termina en vocal).
if l_letter == 'a' or l_letter == 'e' or l_letter == 'i' or l_letter == 'o' or l_letter == 'u' or l_letter == 'A' or l_letter == 'E' or l_letter == 'I' or l_letter == 'O' or l_letter == 'U':
    print(f"{word}!")
else:
    print(f"{word}")

# 8. Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.


print("¡Bienvenido/a!") # Bievenida

name = input("Escribe tu nombre: ") #Solicitamos el nombre al usuario

# Presentamos las opciones:
print("¡Perfecto! Ahora selecciona una de las siguientes opciones:")
print("Digita 1 (uno) para ver tu nombre en mayúsculas")
print("Digita 2 (dos) para ver tu nombre en mayúsculas")
print("Digita 3 (uno) para ver tu nombre en mayúsculas")

option = int(input("Selecciona tu opción: ")) # Solicitamos elija una opción.

# Validamos la opción sea entre los valores propuestos y mostramos el resultado segun la opción.
if option == 1:
    print(name.upper())
elif option == 2:
    print(name.lower())
elif option == 3:
    print(name.title())
else:
    print("Ha ingresado un valor incorrecto, por favor ingrese solo numeros del 1 al 3")

# 9. Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Solicitamos al usuario el dato
escala = float(input("Para ayudarte a calcular la magnitud del terremoto, por favor ingresá la escala: "))

# Evaluamos el dato ingresado por el usuario y comparamos con las escalas de Richter
if escala < 0: # Verificamos ingrese la edad en numeros positivos y mayor que 0, para esta verificación es mejor usar while.
    print("La escala de los terremotos va de 0 (cero) a 7 (siete) por favor ingresa un valor correcto")
elif escala < 3:
    print("Muy leve (imperceptible).")
elif escala >= 3 and escala < 4:
    print("Leve (ligeramente perceptible)")
elif escala >= 4 and escala < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif escala >= 5 and escala < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif escala >= 6 and escala < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif escala >= 7:
    print("Extremo (puede causar graves daños a gran escala).")


# 10. Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
print("¡Bienvenido/a!")
print("Este programa te ayudará a saber cual es la estación del año en el que te encuentras")
print("Para comenzar, indicanos en que hemisferio te encuentras")

h = input("Presiona N para Norte ó S para Sur: ").upper() # Solicitamos el hemisferio y convertimos la letra en mayúscula.

if h != 'N' and h != 'S': # Verificamos no se haya ingresado un valor distinto a los propuestos.
    print("Ha ingresado un valor invalido, por favor presione N para Norte o S para Sur")
    print("Intente de nuevo.")
else:
    day = int(input("¡Genial! ahora dinos qué día es: "))
    if day < 1 or day > 31: # Verificamos el dia no exeda lo permitido
        print("¡Ha ingresado un valor invalido!")
        print("Recordá que los días van del 1 al 31...")
        print("Por favor intenta de nuevo")
    else:
        month = input("Ahora, indicanos qué mes del año es: ").lower() # Solicitamos el mes y lo convertimos a minúsculas
        
        # Convertimos el mes a un número
        if month == 'enero': month = 1
        elif month == 'febrero': month = 2
        elif month == 'marzo': month = 3
        elif month == 'abril': month = 4
        elif month == 'mayo': month = 5
        elif month == 'junio': month = 6
        elif month == 'julio': month = 7
        elif month == 'agosto': month = 8
        elif month == 'septiembre': month = 9
        elif month == 'octubre': month = 10
        elif month == 'noviembre': month = 11
        elif month == 'diciembre': month = 12
        else: # Verificamos el mes ingresado sea correcto
            print("Nombre del mes inválido.")
            month = -1

        if month != -1:
            # Estaciones en el hemisferio Norte
            if h == 'N':
                if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day <= 20):
                    print("¡Es Invierno!")
                elif (month == 3 and day >= 21) or (month in [4, 5]) or (month == 6 and day <= 20):
                    print("¡Es Primavera!")
                elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day <= 20):
                    print("¡Es Verano!")
                elif (month == 9 and day >= 21) or (month in [10, 11]) or (month == 12 and day <= 20):
                    print("¡Es Otoño!")

            # Estaciones en el hemisferio Sur
            elif h == 'S':
                if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day <= 20):
                    print("¡Es Verano!")
                elif (month == 3 and day >= 21) or (month in [4, 5]) or (month == 6 and day <= 20):
                    print("¡Es Otoño!")
                elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day <= 20):
                    print("¡Es Invierno!")
                elif (month == 9 and day >= 21) or (month in [10, 11]) or (month == 12 and day <= 20):
                    print("¡Es Primavera!")