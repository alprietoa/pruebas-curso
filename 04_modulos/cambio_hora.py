import datetime
import pytz



def cambio_fecha_hora_utc(fecha):
    zona_horaria = pytz.timezone('America/Bogota')
#    zona_horaria = pytz.timezone('America/New_York')
#    zona_horaria = pytz.timezone('Europe/Madrid')
#    zona_horaria = pytz.timezone('CET')
#    # hora utc
#    zona_horaria = pytz.timezone('Zulu')
#    zona_horaria = pytz.timezone("UTC")

#    fecha_utc = fecha.replace(tzinfo=pytz.utc).astimezone(zona_horaria)

    # Definimos la zona horaria
    fecha_resultado = fecha.astimezone(zona_horaria)
    return fecha_resultado

def imprime(ejemplo,dt_ini,dt_fin):
	# Imprime el resultado final
	# -----------------------------------------------------
	fecha_texto_ini = dt_ini.strftime('%d/%m/%Y %H:%M %Z %z')
	fecha_texto_fin = dt_fin.strftime('%d/%m/%Y %H:%M %Z %z')
	print(" * " + ejemplo + " : Hora inicial", fecha_texto_ini)
	print(" * " + ejemplo + " : Hora final", fecha_texto_fin)
	print(" ")
	#2018-06-13 15:00:00+00:00



# Ejemplo 1: dt_ini desde un String
fecha = "20180613"
hora = "17"
dt = datetime.datetime.strptime(fecha + hora, "%Y%m%d%H")
# La defino como UTC
dt_ini = dt.replace(tzinfo=pytz.utc)
# Realizamos el cambio de ZONA HORARIA
dt_fin = cambio_fecha_hora_utc(dt_ini)
# final
imprime("Ejemplo 1",dt_ini,dt_fin)

# Ejemplo 2: dt_ini desde un objeto datetime sin zona horaria definida.
dt = datetime.datetime.now()
dt_ini = dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Europe/Madrid"))
# Realizamos el cambio de ZONA HORARIA
dt_fin = cambio_fecha_hora_utc(dt_ini)
# final
imprime("Ejemplo 2",dt_ini,dt_fin)

# Ejemplo 3: dt_ini desde un objeto datetime con zona horaria definida
dt_ini = datetime.datetime.now( pytz.timezone("Europe/Madrid") )
# Realizamos el cambio de ZONA HORARIA
dt_fin = cambio_fecha_hora_utc(dt_ini)
# final
imprime("Ejemplo 3",dt_ini,dt_fin)


dt_ini = datetime.datetime.now( pytz.utc )
zona_horaria = pytz.timezone('America/Bogota')
# Definimos la zona horaria
fecha_resultado = dt_ini.astimezone(zona_horaria)
print(fecha_resultado)
