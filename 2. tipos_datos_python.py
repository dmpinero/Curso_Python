# -*- coding: utf-8
a = "8"
b = 4
print a, b
# print a + b # Python es fuertemente tipado. No pueden sumarse enteros y cadenas.
			# TypeError: cannot concatenate 'str' and 'int' objects

# Python también permite la programación imperativa, programación funcional y programación orientada a aspectos.

############################### Números ###############################
entero = 50
print type(entero) # <type 'int'>

# Puede especificarse que sea un tipo long con L al final
enteroLago = 50L
print type(enteroLago)

# Puede especificarse que sea un tipo octal con 0 al inicio
enteroOctal = 050
print type(enteroOctal)

enteroHexadecimal = 0x17 # Número 23 en decimal
print type(enteroHexadecimal)
print enteroHexadecimal

real = 0.2703
print real

real = 0.1e-3 # Real con notación científica
print real
############################### Números ###############################

############################### Cadenas ###############################
unicode = u"äóè"
print unicode

raw = r"\n" # Las cadenas raw (en inglés, cruda) no sustituyen las \ por su correspondiente carácter (aquí no se cambia por \n por el salto de línea)
print raw

triple = """primera linea
esto se vera en otra linea"""
print triple

a = "uno"
b = "dos"
c = a + b # c es “unodos”
print c
c = a * 3 # c es “unounouno”
print c
############################### Cadenas ###############################

############################### Booleanos ###############################
verdad = True
print type(verdad) # <type 'bool'>

falso = False

print verdad and falso # False
print verdad or falso # True
print not verdad # False

print verdad == falso # False
print not verdad == falso # True
print 7 > 8	# False
print 7 < 8 # True
print 7 != 8 # True

############################### Booleanos ###############################