turistas = {
    "001": ["John Doe", "EEUU", "12-01-2024"],
    "002": ["Emily Smith", "EEUU", "23-03-2024"],
    "003": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "004": ["Maria Lopez", "Mexico", "08-12-2023"]
}

def turistas_por_pais(p):
    r = [v[0] for v in turistas.values() if v[1].lower() == p.lower()]
    print(r if r else "No hay turistas de ese pais.")

def turistas_por_mes(m):
    total = len(turistas)
    c = sum(int(v[2].split("-")[1]) == m for v in turistas.values())
    print(f"El número de turistas equivale al {round(c/total*100, 1)} % del total.")

def eliminar_turista():
    n = input("Nombre a eliminar: ").lower()
    for k in list(turistas):
        if turistas[k][0].lower() == n:
            del turistas[k]
            print("Turista eliminado con éxito.")
            return
    print("Turista no encontrado.")

def main():
    while True:
        print("\\n1.Por país 2.Por mes 3.Eliminar 4.Salir")
        op = input("Opción: ")
        if op == "1": turistas_por_pais(input("País: "))
        elif op == "2":
            while True:
                try:
                    m = int(input("Mes (1-12): "))
                    if 1 <= m <= 12: turistas_por_mes(m); break
                    else: print("Mes inválido.")
                except: print("Ingrese número válido.")
        elif op == "3": eliminar_turista()
        elif op == "4": print("Programa terminado."); break
        else: print("Opción inválida.")

main()
