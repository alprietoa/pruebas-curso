
print("COMPROBADOR DE AÑOS BISIESTOS")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print(f"El año {fecha} es un año bisiesto.")
else:
    print(f"El año {fecha} no es un año bisiesto.")
