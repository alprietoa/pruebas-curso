# -- coding: utf-8 --

archivo=open("observaciones.txt",encoding="utf-8")
lineas=archivo.readlines()
archivo.close()
obs=[]
for linea in lineas:
    campo=linea.replace("\n","").split(";")
    ob={"temperatura":campo[0],"precipitacion":campo[1],"humedad":campo[2],"presion":campo[3]}
    obs.append(ob)
for o in obs:
    print(o)
