# -*- coding: utf-8

############################### if ###############################
fav = "mundogeek.net"
# si (if) fav es igual a "mundogeek.net"
if fav == "mundogeek.net":
	print "Tienes buen gusto!"
	print "Gracias"
############################### if ###############################

############################### if else ###############################
if fav == "mundogeek2.net":
	print "Tienes buen gusto!"
	print "Gracias"
else:
	print "Vaya, que lástima"
############################### if else ###############################

############################### if elif else ###############################
# numero = -2
#numero = 0
numero = 5
if numero < 0:
	print "Negativo"
elif numero > 0:
	print "Positivo"
else:
	print "Cero"
############################### if elif else ###############################

############################### while ###############################
edad = 0
while edad < 18:
	edad = edad + 1
	print "Felicidades, tienes " + str(edad)
############################### while ###############################

############################### buble infinito ###############################
"""
while True:
	entrada = raw_input("> ")
	if entrada == "adios":
		break
	else:
		print entrada
"""
############################### buble infinito ###############################

############################### for in ###############################
secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
	print elemento

for elemento in range(1,10,2): # Número impares del 1 al 10 (salto de 2 en 2)
	print elemento
############################### for in ###############################