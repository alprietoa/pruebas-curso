# -- coding: utf-8 --

print("---------\n ")
print("Parte 1")

valor = input("Introduce un valor")
multiplos = []

primo="si"
for i in range(2,valor):
	if valor % i == 0:
		print( valor, " no es un numero primo.")
		primo="no"
		break

if primo == "si":
    print( valor, " es un numero primo")
