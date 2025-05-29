#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
li = [i for i in range (1, 101) if i % 4 == 0]
print(li)

#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
li5 = [0, "Hola", False, 10, "Último"]
print(li5[-2])

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo:
li_empty = []
li_empty.append("Hola")
li_empty.append("¿Cómo?")
li_empty.append("¿Estás?")
print(li_empty)

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros) #El programa elimina el número de maximo valor en este caso 22 de la lista.

#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
li_num = list(range(10, 31, 5))
list_r = li_num[:2]
print(list_r)

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Fiat"
autos[2] = "Sport"
print(autos)

#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
#Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
#Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
print(compras)

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidad = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(lista_anidad)