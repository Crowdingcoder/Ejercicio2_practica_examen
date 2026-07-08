import os

def limpiar():
    os.system("clear")

#diccionarios
recorridos = {"R001": ["Santiago", "Valparaiso", 120, "normal", "dia", True],
              "R002": ["Santiago", "Concepcion", 500, "cama", "noche", True],
              "R003": ["La Serena", "Coquimbo", 15, "normal", "dia", False]}
ventas= {"R001": [7990,20],
         "R002": [25990,0],
         "R003": [1990,25]}
#validar string
def validar_string(string):
    if len(string) > 0 and string != " ":
        return True
    else:
        print("La casilla no puede estar en blanco.")
        return False
    
#validar mayor o = a 0:
def validar_valor(valor):
    if valor >= 0:
        return True
    else:
        print("El valor no puede ser menor que 0.")

#menu 1
def asientos_origen(origen):
    banderita = False
    acumulador_asientos = 0
    if validar_string(origen):
        for x in recorridos:
            if origen == recorridos[x][0]:
                acumulador_asientos = acumulador_asientos + ventas[x][1]
                banderita = True
        if banderita:
            print(f"El total de asientos disponibles es: {acumulador_asientos}")
        else:
            print("No se encontraron recorridos a su destino.")

#menu 2
def busqueda_precio(p_min,p_max):
    busqueda = []
    banderita2 = False
    for x in ventas:
        if p_min <= ventas[x][0] and p_max >= ventas[x][0]:
            busqueda.append(f"{recorridos[x][0]}-{recorridos[x][1]}--{x}")
            banderita2 = True
    if banderita2:
        busqueda.sort()
        print(f"Los recorridos encontrados son: {busqueda}")
    else:
        print("No se encontraron recorridos.")
            

#menu 3
def buscar_codigo(codigo):
    for x in ventas:
        if codigo == x:
            return True
    return False

def actualizar_precio(codigo,nuevo_precio):
    if buscar_codigo(codigo):
        ventas[codigo][0] = nuevo_precio
        return True
    else:
        return False

#menu 4
def validar_codigo(codigo):
    if buscar_codigo(codigo):
        print("El cofigo ya existe.")
        return False
    else:
        return True
    
def validar_origen(origen):
    if validar_string(origen):
        return True
    else:
        print("Esta mal en algo")
        return False
    
def validar_destino(destino):
    if validar_string(destino):
        return True
    else:
        print("Esta mal en algo")
        return False
    
def validar_distancia(distancia):
    if validar_valor(distancia):
        return True
    else:
        return False
    
def validar_tipo_bus(tipo_bus):
    if tipo_bus == "normal" or tipo_bus == "semi_cama" or tipo_bus == "cama":
        return True
    else:
        print("Opcion no valida")
        return False

def validar_servicio(servicio):
    if servicio == "dia" or servicio == "noche":
        return True
    else:
        print("Es dia o noche mi wacho loco")
        return False
    
def validar_tiene_wifi(tiene_wifi):
    if tiene_wifi == "S" or tiene_wifi == "N":
        return True
    else:
        print("S o N, nada más")
        return False
    
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        print("No puede ser menor o igual que 0, nada gratis las cosas poh.")
        return False
    
def validar_asientos(asientos):
    if validar_valor(asientos):
        return  True
    else:
        return False

def agregar_recorrido(codigo, origen, destino, distancia,tipo_bus, servicio, tiene_wifi, precio,asientos):
    for x in recorridos:
        if codigo == x:
            return False
    recorridos[codigo] = [origen,destino,distancia,tipo_bus,servicio,tiene_wifi]
    ventas[codigo] = [precio,asientos]
    return True

#menu 5
def eliminar_recorrido(codigo):
    if buscar_codigo(codigo):
        ventas.pop(codigo)
        recorridos.pop(codigo)
        return True
    else:
        return False




#leer menu
def leer_opcion():
    while True:
        try:
            menu = int(input("Ingrese opcion:"))
            if menu in range(1,7):
                return menu
        except:
            print("El valor debe ser entero")





