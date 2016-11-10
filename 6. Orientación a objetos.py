# -*- coding: utf-8

############################### Definición de clases ###############################
class Coche:
	""" Abstracción de un coche."""
	def __init__(self, gasolina):
		self.gasolina = gasolina
		print "Tenemos ", gasolina, " litros"

	def arrancar(self):
		if self.gasolina > 0:
			print "Arranca"
		else:
			print "No arranca"

	def conducir(self):
		if self.gasolina > 0:
			self.gasolina -= 1
			print "Quedan", self.gasolina, "litros"
		else:
			print "No se mueve"

miCoche = Coche(3)
miCoche.arrancar()
miCoche.conducir()
############################### Definición de clases ###############################

############################### Herencia ###############################
class Instrumento:
	def __init__(self, precio):
		self.precio = precio
		print "El instrumento genérico cuesta", precio

	def tocar(self):
		print "Estamos tocando música con un instrumento"

	def romper(self):
		print "Eso lo pagas tu"
		print "Son", self.precio, "$$$"

class Bateria(Instrumento):
	def tocar(self):
		print "Estamos tocando música con una Bateria"

class Guitarra(Instrumento):
	pass

instrumento = Instrumento(10)
bateria = Bateria(instrumento)
bateria.tocar()
############################### Herencia ###############################

############################### Herencia múltiple ###############################
class Terrestre:
	def desplazar(self):
		print "El animal anda"

class Acuatico:
	def desplazar(self):
		print "El animal nada"

class Cocodrilo(Terrestre, Acuatico):
	pass

c = Cocodrilo()
c.desplazar() # Se ejecuta el método de la case que esté más a la izquierda en la "importación"
############################### Herencia múltiple ###############################