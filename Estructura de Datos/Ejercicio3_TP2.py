print("=== Aulas ===")

numero_dia = int(input("Ingrese el numero del dia: 1  (lunes) a 6 (sabado): "))

if numero_dia < 1 or numero_dia > 6:
    print("Numero de dia invalido.")
else:
    
    if numero_dia % 2 == 0:  
        aula = "A-300"
    else:  
        aula = "A-315"
    
    print(f"El alumno cursa en el aula {aula} el dia {numero_dia}.")
    
print("\n=== Descuento y Estacionamiento ===")

turno = input("Ingrese el turno: Mañana, Tarde o Noche: ").strip().lower()
materias = int(input("Ingrese la cantidad de materias a inscribir: "))
valor_cuota = float(input("Ingrese el valor de la cuota: "))

if turno == "tarde" and materias > 3:
    descuento = 0.25  
else:
    descuento = 0.05 

cuota_con_descuento = valor_cuota * (1 - descuento)

print(f"El valor de la cuota con descuento es: ${cuota_con_descuento:.2f}")
 

vehiculo = input("Ingrese en el vehiculo que ingresa: Auto, Moto o Bicicleta: ").strip().lower()

if vehiculo == "auto" or vehiculo == "moto":
    costo_estacionamiento = 300
elif vehiculo == "bicicleta":
    costo_estacionamiento = 50
else:
    print("Tipo de vehiculo no valido.")
    costo_estacionamiento = 0
if costo_estacionamiento > 0:
    print(f"El costo diario de estacionamiento es: ${costo_estacionamiento}")
