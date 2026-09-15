# -- coding: utf-8 --

print("---------\n ")
print("Parte 1")

valor = input("Introduce un valor")
multiplos = []
i = 1 
while i < valor:
	if i % 5 == 0:
	    multiplos.append(i)
	i += 1
print("Los multiplos de 5 hasta ", valor , " son : " , multiplos)
