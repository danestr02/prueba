'''Grabar: Corresponde a guardar los datos de un jugador, entre ellos: 
Nombre del jugador, rut, fecha de nacimiento, categoría (Oro – Plata - Bronce), 
celular, identificador de parejas (nombre que le fue asignado a la pareja que compite). 
Además, debe validar que el nombre contenga al menos dos caracteres, que no tenga más de 80 años, 
correo contenga @ y largo mínimo 6.'''

jugadores=[]
nombres=[]
print("1.- Guardar datos del jugador.")
print("2.- Buscar jugador")
print("3.- Imprimir parejas")
print("4.- SALIR")
while True:
    try:
        opc=int(input(":"))
        if 1<=opc<=4:
            break
        else:
            print("Opcion ingresada invalida. Reintente.")
    except:
        print("Error. Reintente.")
if opc==1:
    while True:
        try:
            nombre=input("Ingrese su nombre: ")
            if len(nombre)>=2:  
                nombres.append(nombre)
            else:
                print("El nombre debe tener al menos 2 caracteres. Reintente.")
        except:
            print("Error. Reintente.")
        try:
            rut=input("Ingrese su rut:")
            if len(rut)==8:
                nombres.append(rut)
            else:
                print("El rut debe contener 8 digitos. Reintente")
        except:
            print("Error. Reintente.")

        try:
            fecha_nacimiento=int(input("Ingrese su año de nacimiento: "))
            if fecha_nacimiento>=1965:
                nombres.append(fecha_nacimiento)
            else:
                print("Lo sentimos, usted excede el rango máximo de edad.")
        except:
            print("Error. Reintente.")

        try:
            categoria=int(input("Ingrese la categoria a la que pertenece (1)Oro, (2)plata, (3)bronce: "))
            if 1<=categoria<=3:
                nombres.append(categoria)
            else:
                print("Opcion invalida. Reintente.")
        except:
            print("Error. Reintente.")

        try:
            celular=int(input("Ingrese telefono de contacto: "))
            if len(celular)==9:
                nombres.append(celular)
            else:
                print("El numero de telefono debe tener 9 dijitos. Reintente.")
        except:
            print("Error. Reintente.")

        try:
            correo=input("Ingrese su correo electronico: ")
            if len(correo)==6:
                nombres.append(correo)
            else:
                print("El correo debe tener al menos 6 caracteres. Reintente.")
        except:
            print("Error. Reintente.")

        try:
            id_pareja=input("Ingrese el nombre asignado por parejas: ")
            if len(id_pareja)>=4:
                nombres.append(id_pareja)
            else:
                print("El nombre del equipo debe tener al menos 4 caracteres.")
        except:
            print("Error. Reintente.")
        break
    jugadores.extend([nombres])
    print("Jugador ingresado con exito!")

elif opc==2:
    buscar=int(input("Ingrese el rut del jugador que desea buscar: "))
    for buscar in jugadores:
        if buscar==jugadores:
            print(nombres[0], nombres[3], nombres[4], nombres[5])



