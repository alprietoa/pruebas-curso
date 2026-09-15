# -- coding: utf-8 --


fichero_origen = "origen.txt"
fichero_destino = "destino.txt"


def crear_fichero(fichero_origen):
    f = open(fichero_origen,"w")
    linea =  "Este es un curso sobre Python apasionante." 
    for l in range(100):
       f.write(linea + "\n")
    f.close()

# -----------------------------
# principal #
# -----------------------------
crear_fichero(fichero_origen)
f = open(fichero_origen,"r")
g = open(fichero_destino,"w")
linea = f.readline()
while linea != "":
   g.write(linea)
   linea = f.readline()
g.close()
f.close()
