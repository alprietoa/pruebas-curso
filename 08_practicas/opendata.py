# -*- coding: utf-8 -*-
import json
import os
import datetime
import requests

url = "https://opendata.aemet.es/opendata/api/observacion/convencional/todas/"
akey = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqbWudGVyb2dAYWVtZXQuZXMiLCJqdGkiOiINDRiYmVhMy02NDEyLTQxYWMYmYzOC01MjhlZWJlM2FhMWEiCJleHAiOjE0NzUwNTg3ODcsImlcyI6IkFFTUVUIiwiaWF0IjoNDc0NjI2Nzg3LCJ12VySWQiOiINDRiYmVhMy02NDELTQxYWMtYYzC01jhlZWl2FhWEiLCJy2lIjoIn0.xh3LstTlsP9h5cxz3TLmYF4uJwhOKzA0B6-vH8lPGGw"

# fecha actual en el nombre del fichero con los datos de observación

d = datetime.datetime.now()
ft = "%Y%m%dT%H%M%S%z"
t = datetime.datetime.now().strftime(ft)
# 20220505T090424+0000
fich_name = "observacion_" + t + ".json"

querystring = {"api_key": akey}

headers = {'cache-control': "no-cache"}

#Hacemos la llamada
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

print(response.text)

#Obtenemos el json de la respuesta
data = json.loads(response.text)

estado = data["estado"]

#Si el estado es 200 (exito) obtenemos los datos y los guardamos en un fichero
if (estado == 200):
        
    urlDatos = data["datos"]
    datos = requests.request("GET", urlDatos, headers=headers, params=querystring, verify=False)

    #Insertamos los datos en un fichero
#    fich_datos = open('fich_productos','w')
    fich_datos = open(fich_name,'wb')
    fich_datos.write(datos.content)
    fich_datos.close()
    print( "El fichero de datos esta en: $HOME/scripts_python/bdp/fich_productos")
else:
    print("No se han podido obtener los datos. Codigo de estado: ", estado)

exit(0)

