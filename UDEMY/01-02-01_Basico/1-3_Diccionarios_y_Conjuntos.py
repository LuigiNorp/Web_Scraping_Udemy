#                                   CONJUNTOS
# Son otro tipo de colección que no tienen índices y no almacenan elementos repetidos

conjunto = {1, 5, 9}

# Añadiendo elementos al conjunto
print("\nConjunto original: ", conjunto)
conjunto.add(10)
print("conjunto.add(10) = ",conjunto)
conjunto.add(9)
print("conjunto.add(9) = ",conjunto)
# Removiendo elementos
conjunto.remove(10)
print("conjunto.remove(10) = ", conjunto)

# Recorrer conjunto
print ("\nRecorriendo conjunto elemento por elemento")
for elem in conjunto:
    print (elem)

# Verificar si un valor existe dentro del conjunto
print ("\nSi conjunto contiene 5: ", 5 in conjunto)
print ("Si conjunto contiene 8: ", 8 in conjunto)

# Operaciones entre conjuntos
conjunto2 = {1, 5, 10}
print("\nConjunto: ",conjunto)
print("Conjunto2: ",conjunto2)
print ("Unión entre conjunto y conjunto2: ", conjunto.union(conjunto2))
print ("Intersección entre conjunto y conjunto2: ", conjunto.intersection(conjunto2))

#                                    DICCIONARIOS
# Cada elemento que se almacena dentro de los diccionarios es un par.

diccionario = {
    "nombre": "Marco",
    "edad": 19
}
print ("\nDiccionario completo: ",diccionario)
print ("diccionario['edad'] = ",diccionario["edad"])

# Agregando elemento a diccionario
print ("\nAgregando y eliminando elementos de diccionario")
diccionario["apellido"] = "Perez"
print ('diccionario["apellido"] = "Perez": ', diccionario)
# Eliminando elemento de diccionario
del diccionario["apellido"]
print ('del diccionario["apellido"]: ', diccionario)
# Modificar valor en diccionario
diccionario["edad"] += 20
print ('diccionario["edad"] += 20): ', diccionario)

# Para recorrer un diccionario
print ("\nRecorriendo un diccionario con for")
for clave,valor in list(diccionario.items()):
    print(clave,valor)

# Se pueden anidar diccionarios
d = {
     "nombre": ["Hola Mundo", 19],
     "edad": {
         "edad de papa": 28,
         "nombre 2": "Alonso"
     }
}
print('\nd["edad"]["edad de papa"]: ', d["edad"]["edad de papa"])
print ('d["nombre"][1]: ',d["nombre"][1])