# Diccionario de turistas inicial

turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Sophia Cisternas", "Chile", "04-04-2024"],
    "011": ["Joaquin Dupre", "Chile", "04-04-2024"]
}

# Función para la opción 1
def turistas_por_pais(pais):
    lista = [info[0] for info in turistas.values() if info[1].lower() == pais.lower()]
    if lista:
        print(lista)
    else:
        print("No hay turistas de ese pais.")

# Función para la opción 2
def turistas_por_mes(mes):
    total = len(turistas)
    conteo = 0
    for info in turistas.values():
        fecha = info[2]
        try:
            mes_turista = int(fecha.split("-")[1])
            if mes_turista == mes:
                conteo += 1
        except (IndexError, ValueError):
            continue
    porcentaje = round((conteo / total) * 100, 1)
    return porcentaje

# Función para la opción 3
def eliminar_turista():
    nombre_buscar = input("Ingrese el nombre del turista a eliminar: ").strip().lower()
    for id_turista, info in list(turistas.items()):
        if info[0].strip().lower() == nombre_buscar:
            del turistas[id_turista]
            print("Turista eliminado con éxito.")
            return
    print("Turista no encontrado. No se pudo eliminar.")

# Función principal (main)
def main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")

        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            pais = input("\nIngrese pais a buscar: ").strip()
            turistas_por_pais(pais)
        elif opcion == "2":
            while True:
                try:
                    mes = int(input("\nIngrese mes a buscar: ").strip())
                    if 1 <= mes <= 12:
                        porcentaje = turistas_por_mes(mes)
                        print(f"El número de turistas equivale al {porcentaje} % del total.")
                        break
                    else:
                        print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                except ValueError:
                    print("Debe ingresar un número entero.")
        elif opcion == "3":
            eliminar_turista()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe seleccionar una opción válida.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
