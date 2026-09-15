
# -- coding: utf-8 --

while True:
    nombre = raw_input("Indique su nombre: ")
    if nombre:
        break

print("Su nombre es :" , nombre )


""" El bucle anterior, incluye un condicional anidado que verifica si 
la variable nombre es verdadera (solo será verdadera si el usuario escribe 
un texto en pantalla cuando el nombre  le es solicitado). 
Si es verdadera, el bucle para (break). Sino, seguirá ejecutándose 
hasta que el usuario, ingrese un texto en pantalla."""
