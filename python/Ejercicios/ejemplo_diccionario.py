personas = {}

personas["juan"] = ["gatito83","Masculino"]
personas["roberto"] = ["pollito14","Masculino"]
personas["carolina"] = ["unicornio35","Femenino"]
personas["berta"] = ["manzanita97","Femenino"]

for nombre in personas:
    datos = personas[nombre]
    print("Nombre:", nombre)
    print("Seudonimo:", datos[0])
    print("Genero:", datos[1])
    print("--------------------------")


for nombre, datos in personas.items():
    print("Nombre:", nombre)
    print("Seudonimo:", datos[0])
    print("Genero:", datos[1])
    print("**************************")   