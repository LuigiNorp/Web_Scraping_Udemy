# Es un trozos de codigo con un nombre asociado que me permiten reutilizarlo

# Se crea la función suma
def suma(lista):
    x = 0
    for elem in lista:
        x += elem
    return x

# Se emplea la función suma
# Aquí no está definido x, solo dentro de la función

sumatoria = suma ([1, 2, 3, 4, 5])
print ("La sumatoria es = ", sumatoria)