# -*- coding: utf-8

############################### Listas ###############################
lista1 = [22, True, "cadena", [1, 2]]

print lista1[0] # 22
print type(lista1[0]) # <type 'int'> 

print lista1[1] # True
print type(lista1[1]) # <type 'bool'>

print lista1[2] # cadena
print type(lista1[2]) # <type 'str'>

print lista1[3] # [1,2]
print type(lista1[3]) # <type 'list'>

print lista1[3][0] # 1
print lista1[3][1] # 2

# Slicing. Permite obtener un subconjunto de una lista
l = [99, True, "una lista", [1, 2]]
mi_var = l[0:2] # mi_var vale [99, True]
print mi_var
mi_var = l[0:4:2] # mi_var vale [99, “una lista”]
print mi_var

l = [99, True, "una lista"]
print mi_var[1:] # [99, 'una lista'] Imprime a partir del segundo elemento
mi_var = l[:2] # mi_var vale [99, True]
mi_var = l[:] # mi_var vale [99, True, “una lista”]
print mi_var
mi_var = l[::2] # mi_var vale [99, “una lista”]
print mi_var

l = [99, True, "una lista", [1, 2]]
l[0:2] = [0, 1] # l vale [0, 1, “una lista”, [1, 2]]
print l

l[0:2] = [False] # l vale [False, “una lista”, [1, 2]]
print l
############################### Listas ###############################

############################### Tuplas ###############################
t = (1, 2, True, "python")
print type(t)  # <type 'tuple'>

t = 1, 2, 3, "4"
print type(t)  # <type 'tuple'>

t = (1)
print type(t) # <type 'int'> No lo reconoce como tupla al no llevar ninguna ,
t = (1,)
print type(t) # <type 'tuple'> Lo reconoce como tupla al llevar ,
############################### Tuplas ###############################

############################### Diccionarios ###############################
d = {"Love Actually": "Richard Curtis", 
	 "Kill Bill": "Tarantino",
	 "Amélie": "Jean-Pierre Jeunet"
}
print d
print d["Love Actually"]
############################### Diccionarios ###############################