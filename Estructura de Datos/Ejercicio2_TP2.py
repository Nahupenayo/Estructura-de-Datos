print("=== Universidad de Python ===")

nota_examen1 = float(input("Ingrese la nota del primer examen: "))
nota_examen2 = float(input("Ingrese la nota del segundo examen: "))

promedio = (nota_examen1 + nota_examen2) / 2

if nota_examen2 >= 7:
    print("Aprobo el ultimo examen.")
else:
    print("Desaprobo el ultimo examen.")

if nota_examen2 > nota_examen1:
    print("Mejoro su desempeño.")
elif nota_examen2 == nota_examen1:
    print("Mantuvo su desempeño.")
else:
    print("Empeoro su desempeño.")

if promedio >= 7:
    print("Promociono la materia.")
elif promedio >= 4:
    print("Debe rendir el examen final.")
else:
    print("Debe recursar la materia.")

print(f"Promedio final: {promedio:.2f}")
