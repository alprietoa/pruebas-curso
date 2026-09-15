# -*- coding: utf-8 -*-

import sys
import json

fichero = sys.argv[1]

def leer_archivo_json():
    with open(fichero,'r', encoding='latin-1') as file:
        data = json.load(file)
    
    return data

def obtener_campos_disponibles(data):
    campos_todos = []
    for item in data:
        campos = list(item.keys())
        for c in campos :
            if c not in campos_todos:
                campos_todos.append(c)
    return campos_todos

def seleccionar_campos(campos):
    print("Campos disponibles:")
    for i, campo in enumerate(campos, 1):
        if campo not in ['lon','lat','alt','idema','fint']:
            print(f"{i}. {campo}")
    
    seleccionados = []
    opcion = input("Selecciona los campos que te interesen (separados por coma): ")
    indices_seleccionados = opcion.split(",")
    
    for indice in indices_seleccionados:
        indice = int(indice.strip()) - 1
        if indice >= 0 and indice < len(campos):
            seleccionados.append(campos[indice])

    seleccionados_mas = seleccionados + ['lon','lat','alt','idema','fint']

    return seleccionados_mas


# Uso de las funciones
data = leer_archivo_json()
campos_disponibles = obtener_campos_disponibles(data)
campos_seleccionados = seleccionar_campos(campos_disponibles)
print(campos_seleccionados)

