# diccionario para almacenar las personas
personas = {}

# funcion para agregar una persona
def agregar_persona():
    nombre = input("Ingrese nombre persona: ")
    if nombre in personas:
        print("Esta persona ya esta registrada.")
    else:
        personas[nombre] = "registrado"
        print(f"La persona de nombre '{nombre}' fue agregada exitosamente.")

    for persona in personas:
        print("PERSONAS REGISTRADAS :", persona)  

# funcion para eliminar una persona
def eliminar_persona():
    nombre = input("Ingrese el nombre de la persona que desea eliminar: ")
    if nombre in personas:
        del personas[nombre]
        print(f"La persona de nombre '{nombre}' fue eliminada del registro.")
    else:
        print("Persona no encontrada.")

    for persona in personas:
        print("PERSONAS REGISTRADAS :", persona)      

# funcion principal que ejecuta el menú

while True:
    print("*** Menu ***")
    print("1. Agregar persona")
    print("2. Eliminar persona")
    print("3. Salir")
    opcion = input("Seleccione una opcion del 1 al 3 : ")
    if opcion == "1":
        agregar_persona()
    elif opcion == "2":
        eliminar_persona()
    elif opcion == "3":
        print("programa terminado")
        break
    else:
        print("opcion no valida, pruebe con una del 1 al 3")

