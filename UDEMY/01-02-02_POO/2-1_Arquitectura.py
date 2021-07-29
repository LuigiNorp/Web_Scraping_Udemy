# Programación Orientada a Objetos
# En este ejemplo se asocia la programación orientada a objetos a la arquitectura, considerando
# que para una casa se necesita considerar las siguientes propiedades:

# color
# consumo de luz
# consumo de agua

# CREANDO UNA CLASE DE OBJETO
# Se da de alta la CLASE "Casa"
class Casa:
    # La clase Casa contiene varias funciones

    # Características propias de la CLASE Casa
    def __init__(self, color):
        self.color = color # self sirve para ayuda a asignar el valor de alguna propiedad
        self.consumo_de_luz = 0
        self.consumo_de_agua = 0

    # Una casa se puede pintar
    def pintar (self,color):
        self.color = color

    # En una casa se puede prender la luz
    def prender_luz (self):
        self.consumo_de_luz += 10

    # En una casa se puede abrir la ducha
    def abrir_ducha (self):
        self.consumo_de_agua += 10

    # En una casa se puede tocar el timbre
    def tocar_timbre (self):
        print ("RRIIIIIIIIIIINNG")
        self.consumo_de_luz += 2

# CREANDO Y UTILIZANDO UN OBJETO
# Se construye el OBJETO "mi_casa"
mi_casa = Casa("rojo") # <-- Es necesario dar de alta el parámetro color para definir el objeto
print ("Color del objeto 'mi_casa': ", mi_casa.color)
print ("Consumo de luz inicial del objeto 'mi_casa': ", mi_casa.consumo_de_luz)
print ("Consumo de agua inicial del objeto 'mi_casa: ", mi_casa.consumo_de_agua)
mi_casa.tocar_timbre()
print ("Consumo de luz del objeto 'mi_casa': ", mi_casa.consumo_de_luz)
mi_casa.pintar("verde")
print ("Color del objeto 'mi casa': ",mi_casa.color)

# HEREDANDO CARACTERÍSTICAS A OTRA CLASE DE OBJETOS
class Mansion(Casa):
    # Se superponen algunas de las funcionalidades heredadas de Casa en Mansion
    def prender_luz(self):
        self.consumo_de_luz += 50

    def abrir_ducha(self):
        self.consumo_de_agua += 50

    def tocar_timbre(self):
        print ("DIIIINNNGG DDOOOOONNG")
        self.consumo_de_luz += 3

mi_mansion = Mansion("Blanco")
print ("\nEl color de mi_mansion es: ", mi_mansion.color) # <-- Se reutiliza de la clase Casa
print ("El consumo de luz inicial en mi_mansion es: ", mi_mansion.consumo_de_luz)
mi_mansion.tocar_timbre() #<-- Se modificó en la clase Mansion
print ("El consumo de luz en mi_mansion es: ", mi_mansion.consumo_de_luz)
mi_mansion.pintar("Verde")
print ("El color de mi_mansion es: ", mi_mansion.color)