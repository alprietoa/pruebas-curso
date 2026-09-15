# -- coding: utf-8 --

def primerDigito(numero):
    while numero//10 != 0:
        numero=numero//10
    return numero

def cantidadDivisores(numero):
    cantidad=0
    for n in range(1,numero+1):
        if numero%n == 0:
            cantidad=cantidad+1
    return cantidad

cantidad=0
n=int(input("Número entero:"))
while primerDigito(n)!=9:
    if cantidadDivisores(n)==2:
        cantidad=cantidad+1
    n=int(input("Número entero:"))
print("Tienen sólo 2 divisores:", cantidad, "números")
