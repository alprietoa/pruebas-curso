# -- coding: utf-8 --

print("---------\n ")
print("Parte 1")
MAX_GREETS = 4
num_greets = 0
want_greet = "S"
while want_greet == "S" :
    print( "Hola qué tal!" )
    num_greets += 1
    if num_greets == MAX_GREETS:
            print( "Máximo número de saludos alcanzado" )
            break
    want_greet = input('¿Quiere otro saludo? [S/N]')
print( "Que tenga un buen día" )


# Se prodŕia hacer también así
print("---------\n ")
print("Parte 1, opcion b")
MAX_GREETS=2
while want_greet == "S" and num_questions < MAX_GREETS:
    print( "Hola qué tal!" )


print("---------\n ")
print("Parte 2")
# COMPROBAR LA RUPTURA
# Si el bucle while finaliza normalmente (sin llamada a break) el flujo de control pasa a la sentencia opcional else.
MAX_GREETS = 4
num_greets = 0
want_greet = "S"
while want_greet == "S" :
    print( "Hola qué tal!" )
    num_greets += 1
    if num_greets == MAX_GREETS:
            print( "Máximo número de saludos alcanzado" )
            break
    want_greet = input( "¿Quiere otro saludo? [S/N]" )
else:
    print( "Usted no quiere más saludos" )
print( "Que tenga un buen día" )

print("---------\n ")
print("Parte 3")
# Hay situaciones en las que, en vez de romper un bucle, 
#     nos interesa saltar adelante hacia la siguiente repetición.
want_greet = "S"
valid_options = 0
while want_greet == "S" :
    print( "Hola qué tal!" )
    want_greet = input( "¿Quiere otro saludo? [S/N]" )
    if want_greet not in "SN" :
            print( "No le he entendido pero le saludo" )
            want_greet = "S"
            continue
    valid_options += 1
print( valid_options, "respuestas válidas" )
print( "Que tenga un buen día" )


