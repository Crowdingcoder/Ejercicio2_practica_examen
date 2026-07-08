from functions import *
limpiar()
while True:
    print("===== MENÚ PRINCIPAL =====")
    print("1. Asientos por ciudad de origen")
    print("2. Busqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("===========================================================")
    try:
        menu = leer_opcion()
        if menu == 1:
            print("menu 1")
            origen = input("Ingrese cuidad de origen a consulatar: ").capitalize()
            asientos_origen(origen)
        elif menu == 2:
            print("menu 2")
            try:
                p_min = int(input("Ingrese precio minimo: "))
                while not validar_valor(p_min):
                    p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                while not validar_valor(p_max):
                    p_max = int(input("Ingrese precio maximo: "))
                busqueda_precio(p_min,p_max)
            except:
                print("Debe ingresar valores enteros.")
        elif menu == 3:
             print("Menu 3")
             while True:
                codigo = input("Ingrese codigo del recorrido: ").upper()
                if buscar_codigo(codigo):
                    print("Es el martillo, es real")
                if validar_string(codigo):
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if validar_valor(nuevo_precio):
                        if actualizar_precio(codigo,nuevo_precio):
                            print("Precio actualizado")
                        elif actualizar_precio(codigo,nuevo_precio) == False:
                            print("El codigo no existe")
                pregunta = input("Desea actualizar otro precio(s/n)? ").upper()
                while pregunta != "S" and pregunta != "N":
                    pregunta = input("la respuesta no es valida.\nDesea actualizar otro precio(s/n)? ").upper()
                if pregunta == "S":
                    continue
                elif pregunta == "N":
                    print(ventas)
                    break
        elif menu == 4:
            print("Menu 4")
            codigo = input("Ingrese codigo del recorrido: ").upper()
            if validar_codigo == False:
                break

            origen = input("Ingrese origen: ").capitalize()
            if validar_origen(origen) == False:
                break

            destino = input("Ingrese destino: ").capitalize()
            if validar_destino(destino) == False:
                break
            
            distancia = int(input("Ingrese distancia (KM): "))
            if validar_distancia(distancia) == False:
                break

            tipo_bus = input("Ingrese tipo de bus (normal/semi-cama/cama): ").lower()
            if validar_tipo_bus(tipo_bus) == False:
                break

            servicio = input("Ingrese servicio (dia/noche): ").lower()
            if validar_servicio(servicio) == False:
                break

            tiene_wifi = input("¿Tiene WiFi? (s/n) ").capitalize()
            if validar_tiene_wifi(tiene_wifi) == False:
                break

            if tiene_wifi == "S":
                tiene_wifi = True
            elif tiene_wifi == "N":
                tiene_wifi = False
            
            precio = int(input("Ingrese precio: "))
            if validar_precio(precio) == False:
                break

            asientos = int(input("Ingrese asientos: "))
            if validar_asientos(asientos) == False:
                break

            if agregar_recorrido(codigo, origen, destino, distancia,tipo_bus, servicio, tiene_wifi, precio,asientos):
                print("Recorido agregado")
            elif agregar_recorrido(codigo, origen, destino, distancia,tipo_bus, servicio, tiene_wifi, precio,asientos) == False:
                print("El codigo ya existe")
        
        elif menu == 5:
            print("Menu 5")
            codigo = input("Ingrese codigo").upper()
            if eliminar_recorrido(codigo):
                print("Recorrido eliminado")
                print(recorridos)
            elif eliminar_recorrido(codigo) == False:
                print("Codigo no encontrado")


        elif menu == 6:
            limpiar()
            print("Programa finalizado.")
            break

    except:
         print("Valor ingresado no es valido.")
