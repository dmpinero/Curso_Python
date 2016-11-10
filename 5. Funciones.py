# -*- coding: utf-8

############################### valores por defecto ###############################
def imprimir(texto, veces = 1):
	print veces * texto

imprimir("Hola Dani\n", 6) # Se imprime 6 veces el texto
imprimir("Hola Dani\n") # Se imprime 1 vez el texto
imprimir(veces=3, texto="Hola Dani\n") # Se imprime 3 veces el texto
############################### valores por defecto ###############################

############################### número  variable de argumentos ###############################
def varios(param1, param2, *otros): # La variable otros es una tupla con los parámetros que recibe
	#print "El tipo del parámetro *otros es {0}", type(otros)
	for val in otros:
		print val

varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)

def varios(param1, param2, **otros): # Si se especifica ** indica que se recibe el último parámetro como un diccionario
	for i in otros.items(): # Obtiene las claves
		print i

varios(1, 2, tercero=3)
#varios(1, 2, parametro_variable={"1":"uno", "2":"dos"})
############################### número  variable de argumentos ###############################

############################### paso por referencia de argumentos a funciones ###############################
def f(x, y):
	x = x + 3
	y.append(23)
	print x, y

x = 22 # Los enteros son inmutables (como las tuplas), por lo que se crearía una copia dentro de la función f
y = [22] # Lista. Es mutable
f(x, y)
print x, y
############################### paso por referencia de argumentos a funciones ###############################

############################### Devolución de valores en funciones ###############################
def f(x, y):
	return x * 2, y * 2

a, b = f(1, 2)
print a, type(a)
print b, type(b)
############################### Devolución de valores en funciones ###############################