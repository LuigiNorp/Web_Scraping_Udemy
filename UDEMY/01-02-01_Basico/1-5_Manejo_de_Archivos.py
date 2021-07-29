# Modos de abrir archivo
# r - Read  (Leer)
# a - Add   (Agregar)
# w - Write (Escribir desde cero)


# Creando una función para LEER este archivo en específico
def leer():
    f = open("/01-02-01_Basico/1-5_ManejoArchivos.txt", "r")
    # solo se puede utilizar esta variable una vez
    return f

# Leyendo el archivo
f = leer()
print("\nContenido original del archivo: ", f.readlines())

# Para quitarle los espacios en blanco, separarlo en varias listas
print("\nSin espacios en blanco: ")
file = leer()
for line in file:
    line = line.strip()
    line = line.split(",")
    print(line)

# Se puede acceder a ellos como si fueran listas normales
archivo = leer()
print("\nAccediendo a listas:")
for linea in archivo:
    linea = linea.strip()
    linea = linea.split(",")
    print(linea[0])

# Si queremos AGREGAR nueva información
agregar = open("/01-02-01_Basico/1-5_ManejoArchivos.txt", "a")
agregar.write("Durazno,5,10\n")

# Se puede empezar a escribir un archivo desde cero
escribir = open("/01-02-01_Basico/1-5_Texto2.txt", "w")
escribir.write("HOLA MUNDO")