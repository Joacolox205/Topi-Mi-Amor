personas ={}

def agregar_persona(nombre , seudonimo , genero):
    personas[nombre]= [seudonimo , genero]

def mostrar_persona(nombre):
    del personas [nombre]

while True:
    print("***Menu***")
    print("1)Agregar persona")
    print("2)Mostrar personas registradas")
    print("3)Salir del programa")
    

    opcion= int(input("Ingrese una opcion del 1 al 3 :"))

    if(opcion ==1):
        nombre_persona= input("Ingrese el nombre de la persona:")
        seudonimo_persona=input("Ingrese el seudonimo:")
        genero_persona=input("Ingrese su genero:")
        if nombre_persona in personas:
            print("Esta persona ya ha sido ingresada")
        else:
            agregar_persona(nombre_persona , seudonimo_persona , genero_persona)
            print("La persona" , nombre_persona, "Fue agregada con exito")
        
    elif(opcion ==2):
        for nombre in personas:
            datos = personas[nombre]
            print("Nombre:", nombre)
            print("Seudonimo:", datos[0])
            print("Genero:", datos[1])
            print("--------------------------")
        

    elif(opcion ==3):
        print("programa terminado...")
        break

    else:
        print("la opcion no es valida, pruebe con una del 1 al 3")