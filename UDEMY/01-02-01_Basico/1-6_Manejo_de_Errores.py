# Existe una manera de blindar a tu programa de posibles errores, debido a causas ajenas
# al programador, ya sea una red inadecuada, o defectos en las fuentes. Este método evita
# que el programa termine su ejecución.

cadena = "Hola"

try: # Aquí va la parte riesgosa del código

    x = int(cadena) # <-- El error se debe a que se quiere convertir un texto a int

except Exception as err: # Código que se ejecuta en caso de error

    print("Ha habido un error",err)

print ("He llegado al final")