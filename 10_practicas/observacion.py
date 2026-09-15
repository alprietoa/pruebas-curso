# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime

fichero = sys.argv[1]
fich_salida = "resultado_" + datetime.now().strftime('%Y%m%d_%H%M%S') + ".json"


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
    
    return seleccionados

def guardar_campos_seleccionados(data, campos_seleccionados):
    l_obs = []
    nuevos_datos = {"obs":l_obs}
    
    for item in data:
        nuevo_item = {campo: item.get(campo) for campo in campos_seleccionados}
        nuevo_item['lon'] = item.get('lon')
        nuevo_item['lat'] = item.get('lat')
        nuevo_item['idema'] = item.get('idema')
        nuevo_item['fint'] = item.get('fint')
        l_obs.append(nuevo_item)
    
    with open(fich_salida, 'w') as file:
        json.dump(nuevos_datos, file, indent=4)

# Uso de las funciones
data = leer_archivo_json()
campos_disponibles = obtener_campos_disponibles(data)
campos_seleccionados = seleccionar_campos(campos_disponibles)
guardar_campos_seleccionados(data, campos_seleccionados)


