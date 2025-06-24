# Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
precios_frutas.update({
    'Banana': 1330,
    'Manzana': 1700,
    'Melón': 2800
})
print(precios_frutas)


# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
lista_frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']


# Escribí un programa que permita almacenar y consultar números telefónicos.
def agendar():
    agenda = {}
    for i in range(1, 6):
        nombre = input(f"Ingresá el Nombre {i} para agendar: ")
        numero = input(f"Ingresá el número de {nombre}: ")
        agenda[nombre] = numero
    return agenda

def buscar(agenda, nombre):
    if nombre in agenda:
        print(f"El número de {nombre} es {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no está en tus contactos.")

def main():
    contactos = agendar()

    while True:
        nombre = input("¡Bienvenidx! Ingresá el nombre del contacto a buscar (o escribí salir para terminar): ")
        if nombre.lower() == "salir":
            print("¡Nos vemos pronto!")
            break
        buscar(contactos, nombre)

main()


# Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

def frases():
    frase = input("Ingresá una frase: ")
    palabras = frase.split()
    unicas = set(palabras)

    recuento = {}
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1

    print("Palabras_únicas:", unicas)
    print("Recuento:", recuento)

frases()


# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

def notas_alumnos():
    alumnos = {}

    for i in range(1, 4):
        nombre = input(f"Ingresá el nombre del alumno {i}: ")
        notas = []
        for j in range(1, 4):
            nota = int(input(f"Ingresá nota {j} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)

    print("\nPromedio de cada alumno:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de notas de {nombre} es {promedio:.2f}")

notas_alumnos()


# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

def alumnos_aprobados():
    parcial1_aprobados = set()
    parcial2_aprobados = set()

    for k in range(1, 6):
        nombre = input(f"Ingresá el nombre del alumno {k}: ")
        nota1 = int(input(f"Ingresá nota del Parcial 1 de {nombre}: "))
        nota2 = int(input(f"Ingresá nota del Parcial 2 de {nombre}: "))

        if nota1 >= 6:
            parcial1_aprobados.add(nombre)
        if nota2 >= 6:
            parcial2_aprobados.add(nombre)

    aprobados_ambos = parcial1_aprobados & parcial2_aprobados
    aprobados_solo_uno = parcial1_aprobados ^ parcial2_aprobados
    aprobados_totales = parcial1_aprobados | parcial2_aprobados

    print("\nAprobados en ambos parciales:")
    for alumno in aprobados_ambos:
        print(alumno)

    print("\nAprobados solo en uno de los parciales:")
    for alumno in aprobados_solo_uno:
        print(alumno)

    print("\nTotal de estudiantes que aprobaron al menos un parcial:")
    for alumno in aprobados_totales:
        print(alumno)

alumnos_aprobados()


# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
def agregar_stock(inventario):
    producto = input("Ingresá el nombre del producto: ")
    stock = int(input("Ahora ingresá el stock disponible: "))
    if producto in inventario:
        inventario[producto] += stock
        print(f"Se sumaron {stock} unidades. Ahora hay {inventario[producto]} unidades de {producto}.")
    else:
        inventario[producto] = stock
        print(f"🆕 Producto agregado: {producto} con {stock} unidades.")

def consultar_stock(inventario):
    producto = input("Ingresá el nombre del producto a consultar: ")
    if producto in inventario:
        print(f"Hay {inventario[producto]} unidades disponibles de {producto}.")
    else:
        print("¡Producto inexistente!")

def main_i():
    inventario = {}

    while True:
        print("\n" + "_"*70)
        print("GESTOR DE INVENTARIO")
        print("¿Qué querés hacer hoy?")
        print("1. Consultar stock de un producto")
        print("2. Agregar un producto nuevo o sumar stock")
        print("3. Salir")
        print("_"*70)

        op = int(input("Seleccioná una opción: "))

        if op == 1:
            consultar_stock(inventario)
        elif op == 2:
            agregar_stock(inventario)
        elif op == 3:
            print("¡Hasta la próxima!")
            break
        else:
            print("Marcaste una opción invalida, intentá de nuevo.")

main_i()


# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
def agregar_evento(agenda):
    evento = input("Ingresá el nombre del Evento: ")
    dia = input("Ahora ingresá el stock disponible: ")
    hora = input("Por último digita la hora en formato hh:mm (hora:minutos)")
    agenda[(dia, hora)] = evento
    print(f"Evento '{evento}' agendado para el {dia} a las {hora}.")

def consultar_evento(agenda):
    dia = input("Ingresá el día que querés consultar: ")
    hora = input("Ingresá la hora en formato hh:mm: ")
    clave = (dia, hora)
    if clave in agenda:
        print(f"El {dia} a las {hora} tenés: {agenda[clave]}")
    else:
        print("No tenés ningún evento agendado en ese horario.")

def main_a():
    agenda = {}

    while True:
        print("\n" + "_"*50)
        print("AGENDA PERSONAL")
        print("¿Qué querés hacer hoy?")
        print("1. Consultar eventos")
        print("2. Agregar evento")
        print("3. Salir")
        print("_"*50)

        opcion = int(input("Seleccioná una opción: "))

        if opcion == 1:
            consultar_evento(agenda)
        elif opcion == 2:
            agregar_evento(agenda)
        elif opcion == 3:
            print("¡Hasta la próxima!")
            break
        else:
            print("Marcaste una opción invalida, intentá de nuevo.")

main_a()


# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

invertido = {capital: pais for pais, capital in original.items()}

# Mostrar resultado
print("Original:", original)
print("Invertido:", invertido)