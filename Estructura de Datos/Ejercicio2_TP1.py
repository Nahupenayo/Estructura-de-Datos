import datetime

def es_fecha_valida(dia, mes, año):
    try:
        fecha = datetime.date(año, mes, dia)
        return True
    except ValueError:
      
        return False
if __name__ == "__main__":
    dia = int(input("Introduce el dia: "))
    mes = int(input("Introduce el mes: "))
    año = int(input("Introduce el año: "))
    if es_fecha_valida(dia, mes, año):
        print("La fecha ingresada es valida.")
    else:
        print("La fecha ingresada no es valida.")
