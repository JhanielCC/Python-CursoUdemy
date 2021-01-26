#Definir una clase
class Coche:
    #Atributos o Propiedades(Variables) - Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo ="Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"
    #Constructor - Es un metodo especial  y se suele utilizar para dar valor a los atributos del objeto al crearlo 
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #Métodos, son acciones que hace el objeto (Funciones)
    def getPrivado(self): #SOLO DE ESTA FORMA PODEMOS EXTRAER PROPIEDADES PRIVADAS DE NUESTRA CLASE
        return self.__soy_privado
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
    def getInfo(self):
        info = "------- INFOMACIÓN DEL AUTO ------\n"
        info += "Color: " + self.getColor()
        info += "\nModelo: " + self.getModelo()
        info += "\nMarca: " + self.getMarca()
        info += "\nVelocidad: " + str(self.getVelocidad())
        return info 
#Fin definicion clase