print("=== Listado de Aulas ===")
print("Dia\tAula")

for dia in range(1, 7):  
    if dia % 2 == 0:
        aula = "A-300"  
    else:
        aula = "A-315"  
    print(f"{dia}\t{aula}")

print("\n=== Carga de Edades ===")

cargas_erroneas = 0

while True:
    try:
        edad = int(input("Ingrese una edad mayor de 18 o 0 para finalizar: "))
        if edad == 0:
            break  
        elif edad >= 18:
            print(f"Edad ingresada: {edad}")
        else:
            cargas_erroneas += 1
            print("Debe ingresar una edad valida.")
    except ValueError:
        cargas_erroneas += 1
        print("Debe ingresar un numero valido.")
print(f"\nCargas erroneas realizadas: {cargas_erroneas}")

print("\n=== Promedio de Notas ===")


suma_notas = 0

for i in range(1, 6):  
    nota = float(input(f"Ingrese la nota del alumno {i}: "))
    suma_notas += nota  
promedio = suma_notas / 5
print(f"\nEl promedio de las notas es: {promedio:.2f}")

print("\n=== Costo del Comedor ===")

costo_diario = 1250
for dias in range(1, 7): 
    costo_total = dias * costo_diario
    print(f"{dias} dia(s) cuesta(n) ${costo_total}")
