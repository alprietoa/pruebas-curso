# -- coding: utf-8 --

# Creamos la variable que ir ́a guardando el contenido del archivo . Comienza como string vac  ́ıo.
s = ''

# Abrimos el archivo
archivo = open('archivo_ejemplo.txt','r', encoding='utf-8')

# Leemos el archivo
lineas = archivo.readlines()

# Recorremos la lista de l ́ıneas , quitamos el salto de l ́ınea y lo agregamos al string s
for linea in lineas :
    s = s + linea.strip ('\n')

# Imprimimos
print(s)

# Cerramos el archivo
archivo.close()

#########################################
#### OTRA FORMA DE ESCRIBIR LO MISMO ####
#########################################

# Creamos la variable que ir ́a guardando el contenido del archivo . Comienza como string vac  ́ıo
s = ''

# Abrimos el archivo
with open('archivo_ejemplo.txt','r', encoding ='utf-8') as archivo :
    # Leemos el archiavo
    lineas = archivo.readlines()

# Recorremos la lista de l ́ıneas , quitamos el salto de l ́ınea y lo agregamos al string s
for linea in lineas :
    s = s + linea.strip('\n')

# Imprimimos
print( s )
