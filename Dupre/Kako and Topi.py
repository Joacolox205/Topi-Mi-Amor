import math

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
    "008": ["Sophia Cisternas", "chile", "04-4-2024"],
    "010": ["Joaquin Dupre", "Chile", "04-04-2024"],
    "011": ["Halam Hidalgo", "Venezuela", "07-04-2019"],
}

def turistas_por_pais(pais_buscar):
    """
    Shows a list of tourist names from a specified country.
    The search is case-insensitive for the country name.
    """
    found_turistas = []
    pais_buscar_lower = pais_buscar.lower()
    for turista_info in turistas.values():
        if turista_info[1].lower() == pais_buscar_lower:
            found_turistas.append(turista_info[0])

    if found_turistas:
        print(found_turistas)
    else:
        print("No hay turistas de ese pais.")

def turistas_por_mes():
    """
    Calculates and returns the percentage of tourists who visited Chile in a given month.
    The month input is validated to be between 1 and 12.
    """
    while True:
        try:
            mes_buscar = int(input("Ingrese mes a buscar: "))
            if 1 <= mes_buscar <= 12:
                break
            else:
                print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    count = 0
    total_turistas = len(turistas)
    for turista_info in turistas.values():
        # The date format is DD-MM-YYYY, so the month is at index 1 (0-indexed) after splitting by '-'
        entry_month = int(turista_info[2].split('-')[1])
        if entry_month == mes_buscar:
            count += 1
    
    if total_turistas == 0:
        return "No hay turistas en el sistema para calcular el porcentaje."
    
    percentage = (count / total_turistas) * 100
    return f"El número de turistas equivale al {percentage:.1f} % del total."


def eliminar_turista():
    """
    Allows the user to enter a tourist's name and deletes that tourist if found.
    The deletion is case-insensitive for the tourist's name.
    """
    nombre_a_eliminar = input("Ingrese el nombre del turista a eliminar: ").lower()
    turista_eliminado = False
    keys_to_delete = []

    # Iterate through a copy of keys to avoid RuntimeError: dictionary changed size during iteration
    for key in list(turistas.keys()):
        if turistas[key][0].lower() == nombre_a_eliminar:
            keys_to_delete.append(key)
            turista_eliminado = True
            break # Assuming unique names or only deleting the first occurrence

    if turista_eliminado:
        for key in keys_to_delete:
            del turistas[key]
        print("Turista eliminado con éxito.")
    else:
        print("Turista no encontrado. No se pudo eliminar.")

def buscar_turista_por_nombre():
    """
    Allows the user to search for a tourist by name and displays their full details if found.
    The search is case-insensitive for the tourist's name.
    """
    nombre_buscar = input("Ingrese el nombre del turista a buscar: ").lower()
    found = False
    for key, turista_info in turistas.items():
        if turista_info[0].lower() == nombre_buscar:
            print(f"ID: {key}")
            print(f"Nombre: {turista_info[0]}")
            print(f"País de Origen: {turista_info[1]}")
            print(f"Fecha de Ingreso: {turista_info[2]}")
            found = True
            break
    if not found:
        print("Turista no encontrado.")

def main():
    """
    Main function to run the tourist management system.
    Displays the menu and handles user input for menu options.
    """
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Buscar turista por nombre.") # New option
        print("5.- Salir.") # Option number changed
        
        opcion = input("Ingrese opción: ")

        if opcion == '1':
            pais = input("Ingrese pais a buscar: ")
            turistas_por_pais(pais)
        elif opcion == '2':
            mensaje = turistas_por_mes()
            print(mensaje)
        elif opcion == '3':
            eliminar_turista()
        elif opcion == '4': # New option handling
            buscar_turista_por_nombre()
        elif opcion == '5': # Updated exit option
            print("Programa terminado...")
            break
        else:
            print("Debe seleccionar una opción válida.")

if __name__ == "__main__":
    main()