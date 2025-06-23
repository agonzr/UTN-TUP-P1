# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.
def factorial(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Por favor ingresá el número: "))

if n < 0:
    print("El factorial no se puede calcular con números negativos.")
elif n == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, n + 1):
        print(f"El factorial de {i} es: {factorial(i)}")

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("¿Cuántos términos de Fibonacci querés ver? "))

for i in range(n):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

n = int(input("Ingresá la base: "))
m = int(input("Ingresá el exponente: "))

resultado = potencia(n, m)

print(f"{n} elevado a la {m} es: {resultado}")

# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
def binario(n):
    if n < 2:
        return str(n)
    else:
        return binario(n // 2) + str(n % 2)

n = int(input("Ingresá un número entero positivo: "))

if n < 0:
    print("Por favor ingresá un número positivo.")
else:
    resultado = binario(n)
    print(f"El número {n} en binario es: {resultado}")

# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
def es_palindromo(palabra):
    tildes = "áéíóúÁÉÍÓÚ"

    if any(letra in tildes or letra == " " for letra in palabra):
        return False

    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Ingresá una palabra sin espacios ni tildes: ").lower()

resultado = es_palindromo(palabra)
print(resultado)


# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
n = int(input("Por favor ingrese un número: "))

suma = suma_digitos(n)
print(suma)


# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloq = int(input("Ingresá la cantidad de bloques del ultimo nivel: "))

cant = contar_bloques(bloq)
print(f"Necesitas {cant} bloques para completar la piramide.")


# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

try:
    numero = int(input("Ingresá un número entero positivo: "))
    digito = int(input("Ingresá un dígito entre 0 y 9: "))

    if numero < 0 or not (0 <= digito <= 9):
        print("Entrada inválida. El número debe ser positivo y el dígito debe estar entre 0 y 9.")
    else:
        resultado = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {resultado} vez/veces en el número {numero}.")
except ValueError:
    print("Entrada inválida. Debés ingresar solo números enteros.")