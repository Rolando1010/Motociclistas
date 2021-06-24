from os import replace

nombreArchivo = "Motociclistas/Motociclistas.txt"
tomadosArchivo = "Motociclistas/Tomados.txt"

def generarMotocicletas():
    motos = []
    for i in range(0,12):
        motos += [{"#":i*2+1,"hora":str(i+8)+":00","disponibles":8,"estado":"Disponible"},{"#":i*2+2,"hora":str(i+8)+":30","disponibles":8,"estado":"Disponible"}]
    motos += [{"#":25,"hora":"20:00","disponibles":8,"estado":"Disponible"}]
    return motos

def reiniciarArchivo():
    archivo = open(nombreArchivo,"w")
    for i in range(0,12):
        archivo.write(str(i+8)+":00"+"|8\n")
        archivo.write(str(i+8)+":30"+"|8\n")
    archivo.write("20:00|8")
    archivo.close()

def obtenerMotociclistas():
    archivo = open(nombreArchivo)
    motos = []
    cont = 1
    for linea in archivo:
        datos = linea.split("|")
        motos += [{"#":cont,"hora":datos[0],"disponibles":datos[1].replace("\n",""),"estado":"Disponible" if int(datos[1]) > 0 else 'Ocupados'}]
        cont+=1
    archivo.close()
    return motos

def escribirArchivo(motos):
    archivo = open(nombreArchivo,"w")
    for moto in motos:
        archivo.write(moto["hora"]+"|"+moto["disponibles"])
        if(moto!=motos[-1]):
            archivo.write("\n")
    archivo.close()

def seleccionarMoto(pos,tomar):
    motos = obtenerMotociclistas()
    disponibles = int(motos[pos-1]["disponibles"])
    if tomar:
        disponibles-=1
    else:
        disponibles+=1
    motos[pos-1]["disponibles"] = str(disponibles)
    escribirArchivo(motos)

def tomarQuitarMoto(pos, nombre, tomar):
    archivo = open(tomadosArchivo)
    lineas = archivo.readlines()
    if(tomar):
        if(len(lineas)>0):
            lineas[-1] += "\n"
        lineas += [str(pos)+"|"+nombre]
    else:
        index = lineas.index(str(pos)+"|"+nombre)
        lineas = lineas[:index]+lineas[index+1:]
        if(len(lineas)>0):
            lineas[-1] = lineas[-1].replace("\n","")
    archivo.close()
    archivo = open(tomadosArchivo,"w")
    for i in range(0,len(lineas)):
        archivo.write(lineas[i])
    archivo.close()

def obtenerTomadosUsuario(nombre):
    archivo = open(tomadosArchivo)
    tomados = ""
    for linea in archivo:
        datos = linea.replace("\n","").split("|")
        if(datos[1]==nombre):
            tomados += ","+datos[0]
    return tomados[1:]