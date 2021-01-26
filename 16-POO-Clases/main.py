#Programación Orientada a Objetos POO

#Definir una clase
class Coche:
    #Atributos o Propiedades(Variables) - Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo ="Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    #Métodos, son acciones que hace el objeto (Funciones)
    def acelerar(self): #self paralabre reservada para acceder a las propiedades
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad

    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo
    def setMarca(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
#Fin definicion clase

#Crear Objeto/Instanciar la clase

coche = Coche()
coche.setColor("Negro")
coche.setModelo("Murcielago")

#print(coche)
print("___________Coche 1___________")
print(coche.marca,coche.getModelo(), coche.getColor())
"""
print("Velocidad Actual:    ", coche.getVelocidad())
coche.acelerar()
coche.acelerar()
coche.acelerar()
print("Velocidad Nueva:    ", coche.getVelocidad())
coche.frenar()
print("Velocidad Nueva:    ", coche.getVelocidad())
"""
print("\n___________Coche 2___________")
#Crear más Objetos
coche2 = Coche()
coche2.setColor("Amarillo")
coche2.setMarca("Lamborghini")
coche2.setModelo("Diablo")
print(coche2.marca,coche2.getModelo(), coche2.getColor()) 

print(type(coche2))