# -- coding: utf-8 --

archivo = "mi_texto.txt"
salida = "resulto.txt"

busqueda = input("Ingresa búsqueda: ")
lineas_escribir = []
with open(archivo, "r") as archivo_lectura:
    numero_linea = 0
    for linea in archivo_lectura:
        numero_linea += 1
        linea = linea.rstrip()
        separado = linea.split(" ")
        if busqueda in separado:
            lineas_escribir.append(str(numero_linea) + " - " + linea)

with open(salida, "w") as archivo_salida:
    for linea in lineas_escribir:
        archivo_salida.write(linea + "\n")
