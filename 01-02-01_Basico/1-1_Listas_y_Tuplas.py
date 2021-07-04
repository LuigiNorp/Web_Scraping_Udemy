#                              LISTAS
# Colecciones: Son estructuras donde se pueden almacenar más de un valor
# Listas: Son una coleccion que guardan elementos que guardan un orden
#         entre ellos
print ("\nLISTAS")
#   -->     0   1   2   3   4      De izquierda a derecha
ejemplo = [ 9 , 6 , 1 , 3 , 5 ]
#   <--    -5  -4  -3  -2  -1   De derecha a izquierda

print ("\nLista original completa: ", ejemplo)
print ("\nImprimiendo ejemplo[0] = ", ejemplo[0])
print ("Imprimiendo ejemplo[-1] = ", ejemplo[-1])

print ("\nLista original: ", ejemplo)

# Para añadir un valor usamos append
ejemplo.append(10)
print ("Lista con: ejemplo.append(10) = ", ejemplo)

# Para quitar un valor utilizamos remove
ejemplo.remove(6)
print ("Lista con: ejemplo.remove(6) = ", ejemplo)
# Pop también pero este lo quita por índice, no por valor
ejemplo.pop(-2)
print ("Lista con: ejemplo.pop(-2) = ", ejemplo)

# Para cambiar el valor de un índice
ejemplo[0] = 11
print ("Lista con ejemplo[0] = 11: ", ejemplo)

# Para saber cuantos elementos tiene una lista
print ("\nLista ejemplo modificada: ", ejemplo)
print ("Esta es la longitud de lista ejemplo: ", len(ejemplo))

# Para saber que posición tiene un elemento en la lista
print ("Cual es la posición de 3 en ejemplo: ", ejemplo.index(3))

# Para saber si un elemento se encuentra en la lista
print ("Si 3 está en lista ejemplo: ", 3 in ejemplo)
print ("Si 6 está en lista ejemplo: ", 6 in ejemplo)

# Para ordenar una lista
ejemplo.sort()
print ("\nOrden ascendente: ", ejemplo)
ejemplo.reverse()
print ("Orden inverso: ", ejemplo)

# Recorriendo una lista

numeros = [9, 6, 1, 3, 5]

# Por cada elemento en mi lista, imprimo cada elemento
print ("\nImprimiendo elementos de una lista:")
for elem in numeros:
    print (elem)

# Imprimo elementos de la lista por índice, uno a uno
print ("\nImprimiendo índices de una lista:")
for i in range (len(numeros)):
    print(numeros[i])

#                   CADENAS DE TEXTO
print ("\nSTRINGS")

cadena = "Hola Mundo"

print ("\nCadena : ", cadena)
print ("Longitud de cadena de texto: ",len(cadena),"\n")

# Recorriendo el String
for j in range (len(cadena)):
    print (cadena[j])

# Aplicando funciones

print ("\nMinúsculas: ", cadena.lower())
print ("Mayúsculas: ", cadena.upper())
print ("Primera letra mayúscula: ", cadena.capitalize())

print("\nCadena Original: ", cadena)
print ("Si inicia con hola: ", cadena.startswith("hola"))
print ("Si inicia con Hola: ", cadena.startswith("Hola"))
print ("Si la cadena termina con mundo: ", cadena.endswith("mundo"))
print ("Si la cadena termina con Mundo: ", cadena.endswith("Mundo"))
print ("\nSi solo tiene letras: ", cadena.isalpha()) # falso porque tiene espacio
print ("Si solo tiene numeros: ", cadena.isdigit()) # falso porque tiene letras
print ("Si tiene letras y numeros: ", cadena.isalnum()) # falso porque tiene espacio
print ("Si si todos son mayúsculas: ", cadena.isupper())
print ("Si si todos son minúsculas: ", cadena.islower())

cadena = " Hola Mundo "
print ("\nCadena1: ", cadena)

# Quitar espacios a los lados
print ("Cadena2: ",cadena.strip())

frutas = "Durazo,Manzana,Papaya"

print ("\nfrutas = ", frutas)

separada = frutas.split(",")
print("Separando cadena en listas con split: ",separada)

juntada = "-".join(separada)
print("Juntando las listas en cadenas con join: ", juntada)

#                               TUPLAS
# Las tuplas son listas que no cambian a lo largo de la ejecución del programa

variable = (1, 5, 9)
print ("\nValor de 'variable' es: ",variable)

# Convertir lista en tupla
tupla = tuple(numeros)
print ("\nQue tipo es numeros: ", type(numeros),"\nValor = ", numeros)
print ("Que tipo es tupla: ",type(tupla),"\nValor = ", tupla)
