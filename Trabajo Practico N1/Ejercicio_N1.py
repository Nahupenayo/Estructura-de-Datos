nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")

posee_titulo_secundario = True 

monto_matricula = float(input("Ingrese el monto de la matricula: "))

cuota = monto_matricula + 1000

arancel_python = 12000

costo_mensual = (cuota + arancel_python) / 4 

pago_efectivo = input("Paga en efectivo?: ").lower()

if pago_efectivo == "si":
    costo_mensual *= 0.85 


print("=================================================") 
print("===== Universidad de Python - Inscripciones =====")
print("=================================================")

print("\nDATOS DE INGRESO")
print(f"Nombre completo: {nombre}")
print(f"Edad: {edad}")
print(f"Fecha de nacimiento: {fecha_nacimiento}")
print(f"Posee título?: {posee_titulo_secundario}")
print(f"Matrícula: ${monto_matricula:.2f}")
print(f"Cuota mensual: ${cuota:.2f}")
print(f"Arancel mensual materia Python I: ${arancel_python:.2f}")
print(f"Arancel mensual materia Python I con descuento: ${costo_mensual:.2f}")
